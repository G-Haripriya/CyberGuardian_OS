class PluginRegistry:
    def __init__(self) -> None:
        self._plugins: list[dict] = []

    def list(self) -> list[dict]:
        return list(self._plugins)

    def reload(self) -> None:
        self._plugins = []


plugin_registry = PluginRegistry()
