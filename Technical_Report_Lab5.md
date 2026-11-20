# Laboratory Work 5
## Building a Production-Grade CI/CD Pipeline
## with AI-Specific Security Controls

**Student:** [Full Name]
**Group:** [Group]
**Repository:** https://github.com/Z1ken/vulnfinbot-secure-pipeline

## 1. Objective

The objective of this laboratory work was to
develop a Flask-based financial assistant and
integrate automated security testing into a
GitHub Actions CI/CD pipeline.

The project covers SAST, dependency scanning,
container scanning, DAST and AI-specific tests.

## 2. Application Implementation

The Mini-VulnFinBot application was developed
using Python 3.12 and Flask.

Two main endpoints were implemented:

- GET /health
- POST /api/chat

The application validates incoming JSON,
rejects invalid and oversized messages,
and returns structured JSON responses.

A mock AI response generator was used.

## 3. Automated Testing

The application was tested using pytest.

Application tests: 9
AI security tests: 5
Total tests: 14
Passed: 14
Failed: 0

The tests covered successful requests,
invalid input, missing messages, excessive
message length and AI-related scenarios.

## 4. Security Scanning Results

| Tool | Findings | Severity | Recommendation |
|---|---|---|---|
| Bandit | 0 | None detected | Continue static analysis |
| Semgrep | 0 | None detected | Extend custom rules |
| pip-audit | 0 | None detected | Keep dependencies updated |
| Trivy | 240 records | 48 High, 115 Medium, 68 Low, 9 Unknown, 0 Critical | Review CVEs and update affected packages |
| OWASP ZAP | 1 remaining alert category | Informational | Keep secure caching configuration |
| AI Tests | 5 tests passed | No failures in mock tests | Test a real LLM separately |

## 5. Trivy Vulnerability Analysis

Trivy detected 240 vulnerability records
in the Docker image.

Severity distribution:

- Critical: 0
- High: 48
- Medium: 115
- Low: 68
- Unknown: 9

Affected operating system packages included:

- bsdutils
- libblkid1
- liblastlog2-2
- libmount1
- libsmartcols1
- libuuid1
- login
- mount
- util-linux
- libsqlite3-0

Potential impact includes risks associated
with vulnerable operating system components.

Recommended remediation:

1. Review individual CVE identifiers.
2. Check whether patched versions exist.
3. Update the Python base image.
4. Rebuild and rescan the Docker image.
5. Assess findings without available fixes.

These container vulnerabilities have not yet
been confirmed as remediated.

## 6. OWASP ZAP Analysis

The initial baseline scan identified
five alert categories:

1. Content Security Policy Header Not Set
2. Cross-Origin-Resource-Policy Missing
3. Permissions-Policy Header Not Set
4. X-Content-Type-Options Header Missing
5. Storable and Cacheable Content

The application was updated with:

- Content-Security-Policy
- Cross-Origin-Resource-Policy
- Permissions-Policy
- X-Content-Type-Options
- X-Frame-Options
- Cache-Control: no-store

A root endpoint was also implemented.

The latest local ZAP scan reported:

PASS: 67
FAIL: 0
WARN: 1

The remaining finding was:

Non-Storable Content (Informational).

The number of alert categories decreased
from 5 to 1.

Limitation: The initial scan targeted /health,
while the later scan started at /. This is
a preliminary before/after comparison rather
than an identical-target experiment.

## 7. AI Security Testing

Five AI security scenarios were tested:

### Instruction Override
The mock assistant did not reproduce the
requested instruction override marker.

Result: PASS.

### System Prompt Disclosure
The mock response did not reveal hidden
instructions.

Result: PASS.

### Sensitive Information Disclosure
The synthetic secret marker was not returned.

Result: PASS.

### Unauthorized Tool Usage
The application did not confirm a transfer.
It does not implement banking transactions.

Result: PASS.

### Output Validation
The response remained structured JSON and
did not reproduce the injected script tag.

Result: PASS.

These tests verify limited mock application
behavior. They cannot establish real LLM
prompt injection resistance.

## 8. CI/CD Integration

GitHub Actions was configured to run on pushes
and pull requests targeting the main branch.

The pipeline includes application tests,
AI tests, SAST, dependency auditing,
Docker image building, Trivy and OWASP ZAP.

Scanner reports are collected as workflow
artifacts for later review.

The workflow was also updated to wait for
the Dockerized application to become ready
before starting the ZAP scan.

The latest workflow execution should be
verified for actual scanner success, not only
the overall GitHub Actions status.

## 9. Remediation Summary

Completed changes:

- Added input validation to the Flask API.
- Implemented security-related HTTP headers.
- Added a root endpoint for application access.
- Added Docker non-root execution.
- Added automated application and mock AI tests.
- Improved CI service readiness checks.

Pending security improvements:

- Investigate and remediate Trivy HIGH findings.
- Repeat scans against identical URL targets.
- Test known insecure patterns in an isolated branch.
- Perform real LLM security testing if integrated.
- Expand coverage of the POST /api/chat endpoint.

## 10. Conclusion

The laboratory demonstrates how security
testing can be integrated into automated
software development workflows.

The application passed 14 automated tests,
and six categories of security reports were
created locally.

The OWASP ZAP results improved after the
HTTP security configuration was updated.

Trivy findings remain for further remediation.

The project provides a working educational
CI/CD security pipeline, but additional work
would be necessary for a production deployment.
