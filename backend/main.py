from fastapi import FastAPI

from backend.core.config import settings
from backend.database.engine import database_connected, init_db
from backend.plugin_sdk.registry import plugin_registry

app = FastAPI(title=settings.app_name, version=settings.version)


@app.on_event("startup")
def startup_event() -> None:
    init_db()


@app.get("/health")
def health() -> dict:
    return {
        "status": "healthy",
        "database": "connected" if database_connected() else "disconnected",
        "plugins": len(plugin_registry.list()),
        "version": settings.version,
    }


@app.get("/version")
def version() -> dict:
    return {"version": settings.version}


@app.get("/plugins")
def plugins() -> list:
    return plugin_registry.list()


@app.get("/config")
def config() -> dict:
    return {
        "app_name": settings.app_name,
        "log_level": settings.log_level,
        "plugin_path": settings.plugin_path,
        "database_url": settings.database_url,
    }


@app.post("/plugins/reload")
def reload_plugins() -> dict:
    plugin_registry.reload()
    return {"status": "reloaded", "plugins": len(plugin_registry.list())}
