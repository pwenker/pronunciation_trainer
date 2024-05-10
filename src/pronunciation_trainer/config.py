"""
This file is used to load the OpenAI API key from the .env file.
"""

import os

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

openai_api_key = os.getenv("OPENAI_API_KEY")
