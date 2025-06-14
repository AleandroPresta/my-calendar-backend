import os
import google.generativeai as genai
from google.generativeai.generative_models import GenerativeModel
from google.generativeai.client import configure
from dotenv import load_dotenv
from .config import geminiConfig as config
from ...utils.logging import setup_logging

# Initialize the logger
logger = setup_logging(name="GeminiServiceLogger", level=config["logging"]["level"], path=config["logging"]["path"], filename=config["logging"]["filename"])


class GeminiService:
    """
    Service class for interacting with Gemini API.
    """

    def __init__(self, api_key: str):
        logger.info("[GeminiService.GeminiService.__init__] Initializing GeminiService with provided API key.")
        configure(api_key=api_key)
        logger.debug("[GeminiService.GeminiService.__init__] API key configured successfully.")

        logger.info("[GeminiService.GeminiService.__init__] Creating GenerativeModel instance.")
        self.model: GenerativeModel = GenerativeModel(model_name=config["gemini"]["model_name"])
        logger.debug(f"[GeminiService.GeminiService.__init__] Model instance created: {self.model}")


    def send_message(self, message: str) -> str:
        logger.info("[GeminiService.GeminiService.send_message] Generating content using the model.")
        result = self.model.generate_content(message)
        logger.debug("[GeminiService.GeminiService.send_message] Content generation completed.")
        return result.text

def load_api_key(name: str) -> str:
    """
    Load the API key from environment variables.
    """
    # Load environment variables from .env file in the project root
    project_root: str = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
    logger.debug(f"[GeminiService.load_api_key] Project root directory: {project_root}")
    dotenv_path: str = os.path.join(project_root, '.env')
    logger.debug(f"[GeminiService.load_api_key] Dotenv path: {dotenv_path}")

    logger.info(f'[GeminiService.load_api_key] Searching for .env file at: {dotenv_path}')
    success: bool = load_dotenv(dotenv_path=dotenv_path)
    if not success:
        logger.error(f"[GeminiService.load_api_key] Failed to load environment variables from {dotenv_path}.")
        raise FileNotFoundError(f"[GeminiService.load_api_key] Could not find or load .env file at {dotenv_path}")
    logger.info(f'[GeminiService.load_api_key] Loading API key from environment variable: {name}')

    api_key = os.getenv(name)
    if not api_key:
        logger.error(f"[GeminiService.load_api_key] {name} not found in environment variables.")
        raise ValueError(f"[GeminiService.load_api_key] {name} not found in environment variables.")
    return api_key

def main():
    """
    Main function to run the GeminiService.
    """
    try:
        api_key = load_api_key("GOOGLE_API_KEY")
        logger.info("[GeminiService.main] API key loaded successfully.")
        gemini_service = GeminiService(api_key)
        logger.info("[GeminiService.main] GeminiService initialized successfully.")
        message = "Hello, Gemini!"
        logger.info(f"[GeminiService.main] Sending message to Gemini: {message}")
        response = gemini_service.send_message(message)
        logger.info(f"[GeminiService.main] Received response from Gemini: {response}")
    except Exception as e:
        logger.error(f"[GeminiService.main] An error occurred: {e}")
        raise 

if __name__ == "__main__":
    main()