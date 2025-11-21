import logging
from logging.handlers import RotatingFileHandler
import functools

class LoggerConfig:
    _instance = None
    _configured = False

    def __init__(self, file_name: str, level=logging.INFO):
        if not LoggerConfig._configured:
            self.logger = logging.getLogger(__name__)
            self.logger.setLevel(level)

            if not self.logger.hasHandlers():
                formatter = logging.Formatter(
                    "[%(asctime)s][%(levelname)s][%(message)s]",
                    "%Y-%m-%d %H:%M:%S",
                )
                file_handler = RotatingFileHandler(
                    file_name,
                    maxBytes=10**6,
                    backupCount=6,
                )
                stream_handler = logging.StreamHandler()

                file_handler.setFormatter(formatter)
                stream_handler.setFormatter(formatter)

                self.logger.addHandler(file_handler)
                self.logger.addHandler(stream_handler)
            
            LoggerConfig._configured = True
        else:
            self.logger = logging.getLogger(__name__)
    
    @classmethod
    def get_logger(cls, file_name: str = "app.log"):
        if cls._instance is None:
            cls._instance = cls(file_name)
        return cls._instance.logger
    
    @staticmethod
    def logged(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            logger = LoggerConfig.get_logger()
            logger.info(f"Start {func.__name__} args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            logger.info(f"End {func.__name__} result={result}")
            return result
        return wrapper
