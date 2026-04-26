def validate_config(config: dict) -> bool:
    """
    Validates a configuration dictionary against a set of rules.

    A valid configuration must have:
    - Required keys: 'service_name', 'env', 'port'.
    - 'env' must be one of 'dev', 'staging', 'prod'.
    - 'service_name' must be a non-empty string.
    - 'port' must be an integer between 1 and 65535.

    Args:
        config: A dictionary containing configuration parameters.

    Returns:
        True if the configuration is valid, False otherwise.
    """
    # TODO: Implement the validation logic here.
    # 1. Check if all required keys exist.
    # 2. Check if the 'env' value is one of the allowed environments.
    # 3. Check if 'service_name' is a non-empty string.
    # 4. Check if 'port' is an integer and within the valid range.
    # Remember to return False as soon as a check fails.
    # If all checks pass, return True at the end.
    required_keys = {'service_name', 'env', 'port'}

    if not required_keys.issubset(config):
        return False

    if config['env'] not in ('dev', 'staging', 'prod'):
        return False

    if not isinstance(config['service_name'], str) or not config['service_name'].strip():
        return False

    port = config['port']
    if not isinstance(port, int) or isinstance(port, bool) or not (1 <= port <= 65535):
        return False

    return True    