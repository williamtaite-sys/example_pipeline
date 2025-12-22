Logger Module
=============

This module provides a centralized logging configuration for the pipeline.
It ensures that all logs are formatted consistently and include timestamps.


import sys
from datetime import datetime

class PipelineLogger:
    """
    A simple logger class for the example pipeline.
    """

    def __init__(self, name="Pipeline"):
        """
        Initializes the logger.

        Args:
            name (str): The name of the logger component. Defaults to "Pipeline".
        """
        self.name = name

    def _log(self, level, message):
        """Internal method to print formatted logs."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] [{self.name}]: {message}")

    def info(self, message):
        """
        Logs an informational message.

        Args:
            message (str): The message to log.
        """
        self._log("INFO", message)

    def error(self, message):
        """
        Logs an error message to stderr.

        Args:
            message (str): The error message.
        """
        # Writing to stderr for errors
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        sys.stderr.write(f"[{timestamp}] [ERROR] [{self.name}]: {message}\n")

    def warn(self, message):
        """
        Logs a warning message.

        Args:
            message (str): The warning message.
        """
        self._log("WARN", message)

