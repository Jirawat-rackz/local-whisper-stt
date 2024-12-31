import os
from dotenv import load_dotenv

class Environ:
    def __init__(self):
        load_dotenv()
        self.hf_token = os.environ.get("HUGGINGFACE_TOKEN")
