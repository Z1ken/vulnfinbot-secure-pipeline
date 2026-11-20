from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = 16 * 1024

    from app.routes import main
    app.register_blueprint(main)

    @app.after_request
    def add_security_headers(response):
        response.headers["Content-Security-Policy"] = (
            "default-src 'none'; "
            "frame-ancestors 'none'; "
            "base-uri 'none'; form-action 'none'"
        )
        response.headers["Cross-Origin-Resource-Policy"] = "same-origin"
        response.headers["Permissions-Policy"] = (
            "camera=(), microphone=(), geolocation=()"
        )
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Cache-Control"] = "no-store"
        return response

    return app
