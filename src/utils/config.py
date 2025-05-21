import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "Your_Api_Key")
OPENAI_API_BASE_URL = os.getenv("OPENAI_API_BASE_URL", "Your_base_url")

# Model Configuration
MODEL_NAME = "gpt-4o-mini-2024-07-18"
TEMPERATURE = 0.0

# Application Settings
MAX_SEARCH_RESULTS = 5
MAX_DEFINITIONS = 3 
