"""
logger.py

Centralized logging utility for FactoryBrain AI.
"""

import logging
import os


class Logger:

    def __init__(self, name="FactoryBrainAI"):

        os.makedirs("logs", exist_ok=True)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        if not self.logger.handlers:

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            # File Handler
            file_handler = logging.FileHandler(
                "logs/factorybrain.log"
            )
            file_handler.setFormatter(formatter)

            # Console Handler
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    # ======================================

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def debug(self, message):
        self.logger.debug(message)

    def critical(self, message):
        self.logger.critical(message)


# ======================================
# Demo
# ======================================

if __name__ == "__main__":

    log = Logger()

    log.info("FactoryBrain AI started.")

    log.warning(
        "Document missing metadata."
    )

    log.error(
        "Unable to connect to ChromaDB."
    )

    log.critical(
        "Application crashed unexpectedly."
    )
