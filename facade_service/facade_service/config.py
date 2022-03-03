"""Configs for Flask app."""


class DebugConfig:
    LOGGING_SERVICE_GATEWAY = "http://logging-service-1:5002"
    MESSAGES_SERVICE_GATEWAY = "http://messages-service-1:5003"
