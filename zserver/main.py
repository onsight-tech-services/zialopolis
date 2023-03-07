"""Main entry point for the Zialopolis server."""
import logging

from .db.models import *

logging.basicConfig(level=logging.INFO)

def main():
    """Main entry point for the application."""
    logging.info("Starting Zialopolis server.")

    logging.info("Zialopolis server started.")

if __name__ == "__main__":
    main()
