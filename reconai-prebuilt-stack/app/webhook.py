from flask import Blueprint, request, jsonify

webhook_bp = Blueprint('webhook', __name__)

@webhook_bp.route('/webhook', methods=['POST'])
def receive_webhook():
    data = request.json
    print(f"[WEBHOOK RECEIVED] {data}")
    return jsonify({"status": "received", "echo": data})
