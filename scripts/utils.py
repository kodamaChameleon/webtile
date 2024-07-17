"""
Webtile helper features
"""
import os
import argparse
import socket
import time
from datetime import datetime
import sys
import logging
from logging.handlers import TimedRotatingFileHandler
from dotenv import load_dotenv
from colorama import init, Fore, Style
import frontmatter
from markdown import markdown
from markupsafe import Markup

# Initialize colorama
init()

def get_all_posts(folder: str):
    """
    Fetch all posts from a specified directory
    """
    posts = []
    for filename in os.listdir(folder):
        if filename.endswith('.md'):
            date_str, title = filename.split('_', 1)
            date = datetime.strptime(date_str, '%Y-%m-%d')
            posts.append({'filename': filename, 'title': title[:-3], 'date': date})
    posts.sort(key=lambda x: x['date'], reverse=True)
    return posts

def get_post_content(folder: str, post: dict, length: int=None):
    """
    Render content and metadata from md files
    """
    if "filename" in post and post["filename"].endswith(".md"):
        data = frontmatter.load(f'{folder}/{post["filename"]}')
        post['metadata'] = data.metadata
        if length:
            post['content'] = Markup(markdown(data.content[:length].rsplit(" ",1)[0] + "..."))
        else:
            post['content'] = Markup(markdown(data.content, extensions=['fenced_code']))

    return post

def parse_arguments():
    """
    Handle command line arguments for launcher
    """
    parser = argparse.ArgumentParser(description="Launch the webtile flask application")
    parser.add_argument(
        '-v',
        '--verbose',
        action='store_true',
        help='Enable verbose output for debugging'
    )
    parser.add_argument(
        '-e',
        '--environment',
        type=str,
        default='.env',
        help='Environment file name (default: .env)'
    )

    return parser.parse_args()

class CustomFormatter(logging.Formatter):
    """
    Defines a custom class for logging to include hostname.
    """
    COLORS = {
        logging.DEBUG: Fore.BLUE,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Style.BRIGHT + Fore.RED
    }

    def __init__(self, fmt=None, datefmt=None, style='%', _stdout=False):
        super().__init__(fmt, datefmt, style)
        self._stdout = _stdout

    def format(self, record):
        # Add hostname
        record.hostname = socket.gethostname()
        formatted_message = super().format(record)

        # Add colors
        if self._stdout:
            level_color = self.COLORS.get(record.levelno, Fore.WHITE)
            if level_color:
                formatted_message = f"{level_color}{formatted_message}{Style.RESET_ALL}"

        return formatted_message

def initialize_logger(
        facility,
        log_directory: str="logs",
        log_name: str="webtile.log",
        log_format: str='%(asctime)s %(hostname)s %(name)s.%(levelname)s: %(message)s',
        verbose: bool=False
    ) -> logging.Logger:
    """
    Generate logging for each module.
    - facility: typically best to use __name__ when calling initiate_logger
    - verbose: specify logging at INFO level
    - very_verbose: specify logging at the debug level
    """
    # Configure Logger
    logger = logging.getLogger(facility)
    if verbose:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    # Set Logging Format
    log_path = os.path.join(log_directory, log_name)
    handler = TimedRotatingFileHandler(log_path, when='midnight', interval=1, backupCount=5)
    log_formatter = CustomFormatter(log_format)
    logging.Formatter.converter = time.gmtime
    handler.setFormatter(log_formatter)
    logger.addHandler(handler)

    # Adding a StreamHandler to output to stdout
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_formatter = CustomFormatter(log_format, _stdout=True)
    stdout_handler.setFormatter(stdout_formatter)
    stdout_handler.set_name('StreamHandler')
    logger.addHandler(stdout_handler)

    # Info Logging Started
    log_level = logger.level
    logger.debug(facility +" started logging in mode " + logging.getLevelName(log_level))

    return logger

class Environment:
    """
    Create environment class to handle validation of environmental variables
    """

    def __init__(self, file_path: str='.env') -> None:
        """
        Initialize and load environment
        """
        self.expected_variables = {
            "LOG_DIRECTORY": str,
            "LOG_NAME": str,
            "LOG_FORMAT": str,
            "FEATURED_POST": str
        }
        self.file_path = file_path
        self.load_environment_variables()

    def load_environment_variables(self):
        """
        Validate environmental variables before returning to main process
        """
        load_dotenv(self.file_path, override=True)

        # Validate environmental variables
        for var_name, var_type in self.expected_variables.items():
            if var_name in os.environ:
                if var_type == str and not isinstance(os.getenv(var_name), str):
                    raise ValueError(f"Environment variable {var_name} should be of type {var_type}")
            else:
                raise EnvironmentError(f"Missing required environment variable: {var_name}")

        # Use validated variables
        self.log_directory = os.getenv("LOG_DIRECTORY")
        self.log_name = os.getenv("LOG_NAME")
        self.log_format = os.getenv("LOG_FORMAT")
        self.featured_post = os.getenv("FEATURED_POST")
