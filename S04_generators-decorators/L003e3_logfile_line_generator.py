from pathlib import Path


def read_log_lines(filepath):
    """
    Creates a generator that reads a log file, yielding valid, non-comment lines.

    Args:
        filepath (str): The path to the log file.

    Yields:
        str: A stripped, non-empty, non-comment line from the file.
    """
    with open(filepath, "r") as f:
        for line in f:
            stripped = line.strip()
            if stripped and not stripped.startswith("#"):
                yield stripped


log_path = Path(__file__).parent / "logpruebas.txt"
for linea in read_log_lines(log_path):
    print(linea)