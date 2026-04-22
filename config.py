import os

from dataclasses import dataclass

DEFAULT_HOST = '127.0.0.1'
DEFAULT_PORT = 8080

@dataclass
class Config:
    host: str
    port: int
    debug: bool


def load_config() -> Config:
    return Config(
        host=os.getenv("APP_HOST", DEFAULT_HOST),
        port=int(os.getenv("APP_PORT", DEFAULT_PORT)),
        debug=os.getenv("APP_DEBUG", "false").lower() == "true",
    )