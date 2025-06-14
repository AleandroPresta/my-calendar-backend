from config import promptConfig as config
from ...utils.logging import setup_logging

# Initialize the logger
logger = setup_logging(name=config["logging"]["name"], level=config["logging"]["level"], path=config["logging"]["path"], filename=config["logging"]["filename"])

class PromptService:
    """
    Service class for handling prompt-related operations.
    """
    def generate_prompt(self, user_message: str) -> str:
        """
        Generate a prompt based on the user message.
        """
        logger.info("[PromptService.generate_prompt] Generating prompt.")
        prompt: str = (
            f"User message: {user_message}"
        )
        logger.debug(f"[PromptService.generate_prompt] Generated prompt: {prompt}")
        return prompt