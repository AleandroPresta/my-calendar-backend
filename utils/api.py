from .logging import setup_logging
import os
from dotenv import load_dotenv
from .config import utilsConfig as config

# Initialize the logger
logger = setup_logging(name="ApiUtilsServiceLogger", level=config["logging"]["level"], path=config["logging"]["path"], filename=config["logging"]["filename"])


def load_api_key(name: str) -> str:
    """
    Load the API key from environment variables.
    """
    # Load environment variables from .env file in the project root
    project_root: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    logger.debug(f"[utils.api] Project root directory: {project_root}")
    dotenv_path: str = os.path.join(project_root, '.env')
    logger.debug(f"[utils.api] Dotenv path: {dotenv_path}")

    logger.info(f'[utils.api] Searching for .env file at: {dotenv_path}')
    success: bool = load_dotenv(dotenv_path=dotenv_path)
    if not success:
        logger.error(f"[utils.api] Failed to load environment variables from {dotenv_path}.")
        raise FileNotFoundError(f"[utils.api] Could not find or load .env file at {dotenv_path}")
    logger.info(f'[utils.api] Loading API key from environment variable: {name}')

    api_key = os.getenv(name)
    if not api_key:
        logger.error(f"[utils.api] {name} not found in environment variables.")
        raise ValueError(f"[utils.api] {name} not found in environment variables.")
    return api_key