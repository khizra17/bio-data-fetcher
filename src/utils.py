# src/utils.py
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()  # read .env in project root

def get_env(name, default=None):
    return os.getenv(name, default)

def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)
    return path
