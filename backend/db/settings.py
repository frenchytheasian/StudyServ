from dotenv import load_dotenv

from pathlib import Path
import os

def mongo_uri():
    load_dotenv()

    env_path = Path('.')/'.env'
    load_dotenv(dotenv_path=env_path)

    """ MONGO_URI = os.getenv("MONGO_URI")

    return MONGO_URI """

