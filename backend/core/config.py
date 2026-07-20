from dataclasses import dataclass
from pathlib import Path
import os


@dataclass(frozen=True)
class Settings:
    app_name: str = "CyberGuardian Platform"
    version: str = "0.1.0"
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./database/cyberguardian.db")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    plugin_path: str = os.getenv("PLUGIN_PATH", str(Path("plugins")))


settings = Settings()
