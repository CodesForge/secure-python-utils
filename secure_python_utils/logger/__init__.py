from .simple import LoggerConfig

get_logger = LoggerConfig.get_logger
logged = LoggerConfig.logged

__all__ = ["get_logger", "logged"]