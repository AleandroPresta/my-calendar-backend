import logging

geminiConfig: dict = {
    "logging": {
        "level": logging.DEBUG,
        "path": "api/logs/api/services",
        "filename": "gemini_service.log",
        "name": "GeminiServiceLogger"
    },
    "gemini": {
        "model_name": "models/gemini-1.5-flash",
    }
}

welcomeConfig: dict = {
    "logging": {
        "level": logging.DEBUG,
        "path": "api/logs/api/services",
        "filename": "welcome_service.log",
        "name": "WelcomeServiceLogger"
    }
}

promptConfig: dict = {
    "logging": {
        "level": logging.DEBUG,
        "path": "api/logs/api/services",
        "filename": "prompt_service.log",
        "name": "PromptServiceLogger"
    }
}

bridgeConfig: dict = {
    "logging": {
        "level": logging.DEBUG,
        "path": "api/logs/api/services",
        "filename": "bridge_service.log",
        "name": "BridgeServiceLogger"
    }
}