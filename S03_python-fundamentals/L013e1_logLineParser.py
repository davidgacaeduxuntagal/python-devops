def parse_log_line(log_line: str) -> dict | None:
    """
    Parses a single log line into a structured dictionary.

    The expected log format is: "TIMESTAMP [LOG_LEVEL] MESSAGE"
    Example: "2024-05-20T13:45:10Z [INFO] User 'alice' logged in successfully."

    Args:
        log_line: A string representing a single line from a log file.

    Returns:
        A dictionary containing the 'timestamp', 'log_level', and 'message'
        if the log line is valid, otherwise None.
    """
    if not isinstance(log_line, str) or not log_line:
        return None

    parts = log_line.split(' ', 2)
    if len(parts) < 3:
        return None

    timestamp, log_level_raw, message = parts

    if not (log_level_raw.startswith('[') and log_level_raw.endswith(']')):
        return None

    return {
        'timestamp': timestamp,
        'log_level': log_level_raw[1:-1],
        'message': message,
    }