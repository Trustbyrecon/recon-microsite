from flask import Blueprint, request, jsonify

reflex_bp = Blueprint('reflex', __name__)

@reflex_bp.route('/reflex-score', methods=['POST'])
def compute_reflex_score():
    data = request.json
    output = data.get('output', {})
    base_score = 80
    penalties = 0

    if "hallucination" in output.get("tags", []):
        penalties += 10
    if "slow_response" in output.get("tags", []):
        penalties += 5

    score = base_score - penalties

    return jsonify({
        "reflex_score": score,
        "flags": output.get("tags", []),
        "alignment_ok": score >= 70
    })
