from flask import Blueprint, request, jsonify

ghostlog_bp = Blueprint('ghostlog', __name__)

@ghostlog_bp.route('/ghostlog', methods=['POST'])
def log_ghost_entry():
    data = request.json
    agent_id = data.get('agent_id')
    reflex_score = data.get('reflex_score', 0)
    decision_log = data.get('decision_log', '')
    tags = data.get('tags', [])

    trust_delta = (reflex_score - 80) // 2

    print(f"[GHOSTLOG] Agent: {agent_id}, Score: {reflex_score}, ΔTrust: {trust_delta}")
    print(f"Log: {decision_log} | Tags: {tags}")

    return jsonify({
        "status": "logged",
        "trust_delta": trust_delta
    })
