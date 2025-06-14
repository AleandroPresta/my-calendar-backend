from .config import promptConfig as config
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
            "Role: I want you to be a a translator between the user message and the system data structure.\n"
            "Task: Translate the user message into a structured format that can be used by the system.\n"
            "The user message provided below is used to create, modify or delete an event inside a calendar"
            f"User message: {user_message}\n"
            "Format: Please provide the output in JSON format with the following fields:\n"
            "- operation: A string containing the operation to perform (create, read, update, delete)\n"
            "- event_name: A string containing the name of the event\n"
            "- event_date: A string containing the date of the event in YYYY-MM-DD format\n"
            "- event_time: A string containing the time of the event in HH:MM format\n"
            "Fallback: If the user message does not contain enough information I want you to create" 
            " a JSON object with the operation set to the string 'unknown' and every missing field set to the string 'unknown'.\n"
        )
        logger.debug(f"[PromptService.generate_prompt] Generated prompt: {prompt}")
        return prompt