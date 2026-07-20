from pathlib import Path
import sqlite3

from backend.core.config import settings

DB_PATH = Path("database/cyberguardian.db")
DB_PATH.parent.mkdir(parents=True, exist_ok=True)

_connection = sqlite3.connect(DB_PATH, check_same_thread=False)
_connection.row_factory = sqlite3.Row


def init_db() -> None:
    _connection.execute(
        """
        CREATE TABLE IF NOT EXISTS plugins (
            name TEXT PRIMARY KEY,
            version TEXT NOT NULL,
            type TEXT NOT NULL,
            enabled INTEGER NOT NULL DEFAULT 1
        )
        """
    )
    _connection.commit()


def database_connected() -> bool:
    try:
        _connection.execute("SELECT 1")
        return True
    except sqlite3.Error:
        return False
