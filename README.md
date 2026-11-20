# Mini-VulnFinBot — Secure CI/CD Pipeline

## Project Description

Mini-VulnFinBot is a Python Flask-based financial
assistant developed for Laboratory Work 5.

The project demonstrates how automated security
testing can be integrated into a CI/CD pipeline
using GitHub Actions.

The application uses a mock AI response generator.
A real Large Language Model is not integrated.

## Technologies

- Python 3.12
- Flask
- pytest
- Gunicorn
- Docker
- GitHub Actions
- Bandit
- Semgrep
- pip-audit
- Trivy
- OWASP ZAP

## Project Architecture

The application exposes two main REST endpoints:

GET /health
Returns the application's health status.

POST /api/chat
Accepts a financial question and returns a
structured JSON response.

The application implements request validation,
message length restrictions, error handling
and HTTP security headers.

## Installation

Clone the repository:

git clone https://github.com/Z1ken/vulnfinbot-secure-pipeline.git

cd vulnfinbot-secure-pipeline

Create a Python 3.12 virtual environment:

python3.12 -m venv .venv
source .venv/bin/activate

Install dependencies:

pip install -r requirements.txt

## Running the Application

python run.py

Health check:

curl http://localhost:5000/health

Chat API:

curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message":"How can I manage my budget?"}'

## Automated Testing

Run all tests:

python -m pytest -v

The test suite contains:

- 9 application tests
- 5 AI security tests

Observed result: 14 passed, 0 failed.

## Docker

Build the application image:

docker build -t vulnfinbot:latest .

Run the container:

docker run -d --name vulnfinbot-app \
  -p 127.0.0.1:5001:5000 \
  vulnfinbot:latest

Verify the container:

curl http://localhost:5001/health

## CI/CD Pipeline

GitHub Actions automatically executes the
following steps on push and pull requests:

1. Python environment setup
2. Application unit tests
3. AI security tests
4. Bandit static analysis
5. Semgrep static analysis
6. Dependency scanning with pip-audit
7. Docker image build
8. Trivy image scanning
9. OWASP ZAP baseline scanning
10. Security report artifact upload

Some scanner findings are collected without
blocking the pipeline. A successful workflow
does not guarantee the absence of vulnerabilities.

## Security Tools

Bandit checks Python code for insecure patterns.

Semgrep performs rule-based static analysis
using custom security rules.

pip-audit checks Python dependencies for
publicly reported vulnerabilities.

Trivy scans the Docker image for vulnerabilities.

OWASP ZAP analyzes HTTP responses from
the running web application.

AI security tests evaluate instruction override,
prompt disclosure, sensitive data exposure,
unauthorized actions and output validation.

## Security Reports

Reports are generated in the reports/ directory
and uploaded as GitHub Actions artifacts.

The main files are:

- bandit-report.json
- semgrep-report.json
- dependency-report.json
- trivy-report.json
- zap-report.json
- ai-security-report.md

To download CI-generated reports:

Open GitHub -> Actions -> Select a workflow run
-> Artifacts -> vulnfinbot-security-reports.

## Security Findings

Initial checks showed:

Bandit: 0 findings.
Semgrep: 0 findings.
pip-audit: no known vulnerabilities found.

Trivy reported 240 vulnerability records,
including 48 HIGH and 0 CRITICAL findings.

Initial OWASP ZAP testing reported 5 alert
categories. After security header improvements,
the latest local scan reported 1 informational
alert category.

These ZAP results used different starting URLs,
so they are not a strict like-for-like comparison.

The remaining Trivy findings require analysis,
base-image updates and repeat scanning.

## AI Security Limitations

The application uses mock AI responses.

Passing the AI tests does not demonstrate
resistance to prompt injection in a real LLM.

The application does not execute bank transfers,
access real customer records or invoke external
banking tools.

## Conclusion

Mini-VulnFinBot demonstrates a security-focused
CI/CD workflow integrating application testing,
static analysis, dependency scanning, container
scanning, dynamic testing and mock AI testing.

Additional vulnerability remediation and testing
with a real model would be required before
production deployment.
