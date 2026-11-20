from flask import Blueprint, jsonify, request

main = Blueprint("main", __name__)
MAX_MESSAGE_LENGTH = 1000


@main.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


@main.route("/api/chat", methods=["POST"])
def chat():
    if not request.is_json:
        return jsonify({"error": "JSON required"}), 400

    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    message = data.get("message")

    if not isinstance(message, str):
        return jsonify({"error": "Invalid message"}), 400

    message = message.strip()

    if not message:
        return jsonify({"error": "Empty message"}), 400

    if len(message) > MAX_MESSAGE_LENGTH:
        return jsonify({"error": "Message too long"}), 413

    if "budget" in message.lower():
        response = "Start by tracking your income and expenses."
    elif "save" in message.lower():
        response = "Set a savings goal and save regularly."
    else:
        response = "I can help with basic financial questions."

    return jsonify({"response": response}), 200


@main.route("/", methods=["GET"])
def index():
    return jsonify({
        "application": "Mini-VulnFinBot",
        "status": "running"
    }), 200
