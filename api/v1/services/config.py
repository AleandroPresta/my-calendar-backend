import logging

geminiConfig: dict = {
    "logging": {
        "level": logging.DEBUG,
        "path": "logs/api/services",
        "filename": "gemini_service.log"
    },
    "gemini": {
        "model_name": "models/gemini-1.5-flash",
    }
}

welcomeConfig: dict = {
    "logging": {
        "level": logging.DEBUG,
        "path": "logs/api/services",
        "filename": "welcome_service.log"
    }
}