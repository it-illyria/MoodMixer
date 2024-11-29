import logging
from devcycle_python_sdk import DevCycleCloudClient, DevCycleCloudOptions
from backend.config import Config

# Logging setup
logger = logging.getLogger(__name__)

# Initialize DevCycle Client
cloud_options = DevCycleCloudOptions(enable_edge_db=True)
client = DevCycleCloudClient(Config.DEVCYCLE_SDK_KEY, cloud_options)


def get_feature_flag(flag_key: str, default_value: bool):
    """
    Retrieve the value of a feature flag.
    :param flag_key: The key of the flag to retrieve.
    :param default_value: The default value to return if the flag is not found.
    :return: Boolean value of the flag.
    """
    try:
        # Default user object for flag evaluation (can be extended)
        value = client.variable_value(flag_key, default_value)
        logger.info(f"Flag '{flag_key}' evaluated to: {value}")
        return value
    except Exception as e:
        logger.error(f"Error retrieving flag '{flag_key}': {e}")
        return default_value


def set_feature_flag(flag_key: str, state: bool):
    """
    DevCycle does not directly allow setting feature flags programmatically in production.
    Instead, configure flags via the DevCycle Dashboard for controlled rollout.
    Here, we simulate the toggle for local development purposes.
    """
    logger.warning("Flag changes should be managed in DevCycle Dashboard.")
    # Simulated response
    return {"message": f"Flag '{flag_key}' simulated set to {state}"}
