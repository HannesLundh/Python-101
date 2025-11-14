from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict
import json


class ConfigError(Exception):
    """Raised when the configuration file is invalid or missing required values."""


@dataclass
class AppConfig:
    """Application configuration settings."""
    app_name: str
    environment: str
    log_level: str
    retry_count: int


def read_json_file(path: Path) -> Dict[str, Any]:
    """Read a JSON file and return its contents as a dictionary."""
    if not path.exists():
        raise ConfigError(f"Config file not found: {path}")

    with path.open("r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as exc:
            raise ConfigError(f"Config file is not valid JSON: {path}") from exc


def validate_raw_config(raw: Dict[str, Any]) -> None:
    """
    Validate that the raw config contains required fields
    and that values are of the expected type.

    TODO:
      - Check that app_name, environment, log_level, retry_count exist.
      - Ensure retry_count is an int and >= 0.
      - Optionally validate environment is one of: "dev", "test", "prod".
      - Raise ConfigError with helpful messages when invalid.
    """
    # TODO: implement validation logic
    raise NotImplementedError("validate_raw_config is not implemented yet")


def parse_config(raw: Dict[str, Any]) -> AppConfig:
    """
    Convert a raw config dictionary into an AppConfig object.

    Assumes raw has already been validated.
    """
    return AppConfig(
        app_name=raw["app_name"],
        environment=raw["environment"],
        log_level=raw["log_level"],
        retry_count=int(raw["retry_count"]),
    )


def load_config(path: Path) -> AppConfig:
    """
    High-level API: load and validate config from a JSON file.

    TODO:
      - Use read_json_file to get raw config.
      - Call validate_raw_config.
      - Convert to AppConfig via parse_config.
      - Return the AppConfig.
    """
    # TODO: implement this function
    raise NotImplementedError("load_config is not implemented yet")


def main() -> None:
    """
    Simple manual test:
      - Loads 'appsettings.json' from the appsettings folder. Can change to the other json files to test error handling.
      - Prints the resulting AppConfig.
    """
    config_path = Path(__file__).parent / "appsettings" / "appsettings.json"
    config = load_config(config_path)
    print(config)


if __name__ == "__main__":
    main()
