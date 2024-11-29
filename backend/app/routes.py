from flask import Blueprint, jsonify
from .services.feature_flags import get_feature_flag, set_feature_flag
import logging

# Logger setup
logger = logging.getLogger(__name__)

# Flask Blueprint
main_bp = Blueprint('main', __name__)

# Supported flags
VALID_FLAGS = ["rainbow_mode", "confetti_button", "party_mode", "beginner_mode", "expert_mode"]


@main_bp.route('/', methods=['GET'])
def home():
    """
    Root endpoint.
    """
    return jsonify({"message": "Welcome to MoodMixer API!"}), 200


@main_bp.route('/api/flags', methods=['GET'])
def get_all_flags():
    """
    Get all feature flags and their states.
    """
    try:
        flags = {flag: get_feature_flag(flag, False | True) for flag in VALID_FLAGS}
        return jsonify(flags), 200
    except Exception as e:
        logger.error(f"Error fetching flags: {e}")
        return jsonify({"error": "Failed to fetch flags"}), 500


@main_bp.route('/api/<flag>/<state>', methods=['POST'])
def toggle_flag(flag, state):
    """
    Simulate setting a feature flag.
    """
    if flag not in VALID_FLAGS:
        return jsonify({"error": f"Flag '{flag}' not found."}), 404

    try:
        state_bool = state.lower() == 'true'
        result = set_feature_flag(flag, state_bool)
        return jsonify(result), 200
    except Exception as e:
        logger.error(f"Error setting flag '{flag}': {e}")
        return jsonify({"error": "Failed to set flag."}), 500


@main_bp.route('/api/party-mode', methods=['GET'])
def party_mode():
    if get_feature_flag("party_mode", False):
        return jsonify({"message": "Party mode is enabled!"}), 200
    return jsonify({"message": "Party mode is disabled."}), 200
