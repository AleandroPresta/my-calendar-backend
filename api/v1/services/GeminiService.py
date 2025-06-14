import os
import google.generativeai as genai
from google.generativeai.generative_models import GenerativeModel
from google.generativeai.client import configure
from dotenv import load_dotenv
from .config import geminiConfig as config
from ...utils.api import load_api_key
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