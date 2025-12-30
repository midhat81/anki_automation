from dotenv import load_dotenv
import os

load_dotenv()

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
SERP_API_KEY = os.getenv("SERP_API_KEY")
print("Loaded DEEPL_API_KEY:", DEEPL_API_KEY)
print("Loaded SERP_API_KEY:", SERP_API_KEY)