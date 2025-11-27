# run.py — project entrypoint
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
SRC_PATH = PROJECT_ROOT / "src"
sys.path.insert(0, str(SRC_PATH))

from cli import main

if __name__ == "__main__":
    main()
