from flask import request, jsonify


MAX_MESSAGE_LENGTH = 1000


def register_routes(app):

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify({"status": "healthy"}), 200

    @app.route("/api/chat", methods=["POST"])
    def chat():

        if not request.is_json:
            return jsonify({"error": "Content-Type must be application/json"}), 415

        data = request.get_json(silent=True)

        if not isinstance(data, dict):
            return jsonify({"error": "Invalid JSON request"}), 400

        message = data.get("message")

        if not isinstance(message, str):
            return jsonify({"error": "Message must be a string"}), 400

        message = message.strip()

        if not message:
            return jsonify({"error": "Message cannot be empty"}), 400

        if len(message) > MAX_MESSAGE_LENGTH:
            return jsonify({"error": "Message is too long"}), 400

        response = (
            "You can start by tracking your income and expenses."
        )

        return jsonify({"response": response}), 200

    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal server error"}), 500