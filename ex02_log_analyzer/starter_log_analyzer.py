from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional


@dataclass(frozen=True)
class LogEntry:
    """Represents a single parsed log entry."""
    level: str
    message: str


def read_log_lines(path: Path) -> List[str]:
    """
    Read all lines from a log file.

    This function is intentionally simple and side-effectful.
    """
    with path.open("r", encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


def parse_log_line(line: str) -> Optional[LogEntry]:
    """
    Parse a single log line into a LogEntry.

    Expected line format:
      [INFO] Application started
      [ERROR] Something went wrong

    TODO:
      - Extract level (INFO, WARN, ERROR, etc.) between '[' and ']'.
      - Everything after the closing ']' and a space is the message.
      - Return None if the line does not match the expected format.
    """
    # TODO: implement parsing
    raise NotImplementedError("parse_log_line is not implemented yet")


def count_by_level(entries: Iterable[LogEntry]) -> Dict[str, int]:
    """
    Count how many log entries exist per level.

    Example output:
      {"INFO": 10, "ERROR": 3}
    """
    counts: Dict[str, int] = {}

    # TODO:
    #  - Iterate entries.
    #  - Use dict get / setdefault or similar.
    #  - Return counts.
    raise NotImplementedError("count_by_level is not implemented yet")


def top_n_levels(counts: Dict[str, int], n: int) -> Dict[str, int]:
    """
    Return the top N log levels by frequency.

    TODO:
      - Sort counts by value descending.
      - Take first n items.
      - Return a new dict.
    """
    # TODO: implement
    raise NotImplementedError("top_n_levels is not implemented yet")


def analyze_log(path: Path, n: int = 3) -> Dict[str, int]:
    """
    High-level helper that:
      - Reads the log file
      - Parses each line into LogEntry objects (skipping invalid lines)
      - Counts entries per level
      - Returns the top N levels by frequency

    This function should be easy to unit test.
    """
    lines = read_log_lines(path)
    entries = [
        entry for line in lines
        if (entry := parse_log_line(line)) is not None
    ]
    counts = count_by_level(entries)
    return top_n_levels(counts, n)


def main() -> None:
    """
    Manual test:
      - Analyze 'sample.log' in the same folder.
      - Print the top 3 log levels.
    """
    log_path = Path(__file__).parent / "sample.log"
    result = analyze_log(log_path, n=3)
    print("Top log levels:", result)


if __name__ == "__main__":
    main()
