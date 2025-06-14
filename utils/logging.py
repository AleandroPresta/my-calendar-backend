import logging
from pathlib import Path

def setup_logging(
    name: str = __name__, level: int = logging.DEBUG, path: str = 'logs', filename: str = 'service.log'
) -> logging.Logger:
    """
    Set up logging. File handler logs from 'level', console handler logs ERROR and above.
    Logs will include timestamps.

    Args:
        name: The name of the logger.
        level: The logging level for the logger itself and the file handler.

    Returns:
        The configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(level) # Set the logger's threshold

    # Clear existing handlers to prevent duplicate logs if called multiple times
    if logger.hasHandlers():
        logger.handlers.clear()

    # Create a formatter that includes date and time
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Create a stream handler for console output
    # This handler will only show ERROR and CRITICAL messages
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.ERROR) # Set console handler to ERROR level
    stream_handler.setFormatter(formatter) # Apply formatter to console
    logger.addHandler(stream_handler)

    # Create a file handler to write logs to a file
    # This handler will log messages from the 'level' argument
    log_dir = Path(__file__).resolve().parent.parent / path
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file_path = log_dir / filename

    file_handler = logging.FileHandler(log_file_path)
    file_handler.setLevel(level) # File handler uses the general level
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger