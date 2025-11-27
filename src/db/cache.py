# src/db/cache.py
import sqlite3
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DB_DIR = ROOT / "src" / "db"
DB_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DB_DIR / "cache.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        """
        CREATE TABLE IF NOT EXISTS cache (
            id TEXT PRIMARY KEY,
            source TEXT,
            retrieved_at TEXT,
            filepath TEXT
        )
        """
    )
    conn.commit()
    conn.close()

def cache_result(id_, source, filepath):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute(
        "REPLACE INTO cache (id, source, retrieved_at, filepath) VALUES (?, ?, ?, ?)",
        (id_, source, datetime.utcnow().isoformat(), str(filepath)),
    )
    conn.commit()
    conn.close()

def get_cached(id_):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("SELECT id, source, retrieved_at, filepath FROM cache WHERE id = ?", (id_,))
    row = c.fetchone()
    conn.close()
    return row
