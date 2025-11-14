from __future__ import annotations

from pathlib import Path
from typing import Sequence, List
import json


def load_values(path: Path) -> List[float]:
    """
    Load metric values from a JSON file.

    Expected JSON format:
      [
        {"value": 1.0},
        {"value": 2.5},
        ...
      ]

    TODO:
      - Open the file using a context manager (`with`).
      - Parse JSON.
      - Extract "value" from each entry and return a list of floats.
      - Raise appropriate exceptions on errors (e.g., FileNotFoundError,
        json.JSONDecodeError, KeyError).
    """
    # TODO: implement
    raise NotImplementedError("load_values is not implemented yet")


def calculate_average(values: Sequence[float]) -> float:
    """
    Calculate the arithmetic mean of a sequence of numbers.

    TODO:
      - Return the average of values.
      - Decide what to do for an empty sequence
        (e.g., raise ValueError with a clear message).
    """
    # TODO: implement
    raise NotImplementedError("calculate_average is not implemented yet")


def main() -> None:
    """
    Entry point for the metrics script.

    TODO:
      - Determine the path to 'metrics.json' (e.g., same folder as this file).
      - Load values using load_values.
      - Calculate the average.
      - Print the result using an f-string.
      - Handle exceptions gracefully and print a helpful message instead
        of using exit(1).
    """
    # TODO: implement
    raise NotImplementedError("main is not implemented yet")


if __name__ == "__main__":
    main()
