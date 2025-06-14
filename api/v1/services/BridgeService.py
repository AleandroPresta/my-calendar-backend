from .GeminiService import GeminiService
from .PromptService import PromptService
from .config import bridgeConfig as config
from ...utils.api import load_api_key
from ...utils.logging import setup_logging

# Initialize the logger
logger = setup_logging(name=config["logging"]["name"], level=config["logging"]["level"], path=config["logging"]["path"], filename=config["logging"]["filename"])


"""
    Service that bridges the PromptService and the GeminiService.
"""
class BridgeService:
    def __init__(self, prompt_service: PromptService, gemini_service: GeminiService):
        self.prompt_service = prompt_service
        self.gemini_service = gemini_service

    def bridge(self, user_message: str) -> str:
        """
        Bridges the user message through the prompt service and sends it to the Gemini service.
        """
        try:
            logger.info("[BridgeService.bridge] Bridging user message to Gemini service.")
            # Generate the prompt using the PromptService
            logger.debug(f"[BridgeService.bridge] User message: {user_message}")
            prompt = self.prompt_service.generate_prompt(user_message)
            # Send the generated prompt to the GeminiService
            response = self.gemini_service.send_message(prompt)
            logger.info(f"[BridgeService.bridge] Received response from Gemini service: {response}")
            return response
        except Exception as e:
            raise RuntimeError(f"An error occurred while bridging services: {e}")
        

def main() -> None:
    try:
        api_key = load_api_key("GOOGLE_API_KEY")
        logger.info("[BridgeService.main] API key loaded successfully.")
        gemini_service = GeminiService(api_key)
        logger.info("[BridgeService.main] GeminiService initialized successfully.")
        prompt_service = PromptService()
        logger.info("[BridgeService.main] PromptService initialized successfully.")
        bridge_service = BridgeService(prompt_service, gemini_service)
        logger.info("[BridgeService.main] BridgeService initialized successfully.")
        user_message = input("[BridgeService.main] Please enter your message: ")
        response = bridge_service.bridge(user_message)
        print(f"[BridgeService.main] Response from Gemini: {response}")
    except Exception as e:
        logger.error(f"[BridgeService.main] An error occurred: {e}")
        raise

if __name__ == "__main__":
    main()