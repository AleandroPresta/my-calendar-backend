from .GeminiService import GeminiService
from ...utils.api import load_api_key
from ...utils.logging import setup_logging
from .config import welcomeConfig as config

# Initialize the logger
logger = setup_logging(name="WelcomeServiceLogger", level=config["logging"]["level"], path=config["logging"]["path"], filename=config["logging"]["filename"])

class WelcomeService:
    """
    Service class for generating welcome messages.
    """

    def __init__(self):
        try:
            api_key = load_api_key("GOOGLE_API_KEY")
            logger.info("[WelcomeService.__init__] API key loaded successfully.")
            self.gemini_service = GeminiService(api_key)
            logger.info("[WelcomeService.__init__] GeminiService initialized successfully.")
        except Exception as e:
            logger.error(f"[WelcomeService.__init__] An error occurred: {e}")
            raise

    def get_welcome_message(self) -> str:
        message = "Hello, Gemini!"
        logger.info(f"[WelcomeService.get_welcome_message] Sending message to Gemini: {message}")
        response = self.gemini_service.send_message(message)
        logger.info(f"[WelcomeService.get_welcome_message] Received response from Gemini: {response}")
        return response