# Exercise 01 – Config Loader & Validator

**Goal:**  
Practice Python style, type hints, dataclasses, and exceptions by
building a small, reusable configuration loader.

Here are some official docs
that are useful while you work.

---

## 🔗 Useful Python Documentation

### 📘 Core Language & Style

- Python Tutorial (good overview) → https://docs.python.org/3/tutorial/
- Style guide (PEP 8) → https://peps.python.org/pep-0008/

### 🧱 Dataclasses, Types & Exceptions

- `dataclasses` → https://docs.python.org/3/library/dataclasses.html
- Type hints (`typing`) → https://docs.python.org/3/library/typing.html
- Exceptions & error handling → https://docs.python.org/3/tutorial/errors.html

### 📦 Standard Library Tools Used in This Exercise

- `pathlib.Path` (file paths) → https://docs.python.org/3/library/pathlib.html
- `json` (JSON encode/decode) → https://docs.python.org/3/library/json.html

---

## Files

- `starter_config_loader.py` – starter with TODOs
- `solution_config_loader.py` – reference solution

---

## Your Tasks

### 1. Implement `validate_raw_config(raw: Dict[str, Any]) -> None`

Responsibilities:

- Ensure the following keys exist in `raw`:
  - `app_name`
  - `environment`
  - `log_level`
  - `retry_count`
- Validate:
  - `retry_count` can be converted to an `int`
  - `retry_count >= 0`
- (Stretch) Validate that:
  - `environment` is one of: `"dev"`, `"test"`, `"prod"`
  - `log_level` is one of: `"DEBUG"`, `"INFO"`, `"WARN"`, `"WARNING"`, `"ERROR"`, `"CRITICAL"`
- Raise `ConfigError` with **clear, helpful messages** when validation fails.

Useful docs:

- Exceptions → https://docs.python.org/3/tutorial/errors.html
- `int()` conversion → https://docs.python.org/3/library/functions.html#int

---

### 2. Implement `load_config(path: Path) -> AppConfig`

Steps:

1. Use `read_json_file(path)` (already provided) to read the JSON file into a `dict`.
2. Call `validate_raw_config(raw)` to ensure the config is valid.
3. Call `parse_config(raw)` to convert the dict into an `AppConfig` dataclass.
4. Return the resulting `AppConfig` instance.

Concepts involved:

- `Path` and file handling → https://docs.python.org/3/library/pathlib.html
- JSON to dict conversion → https://docs.python.org/3/library/json.html

---

### 3. Add a simple `if __name__ == "__main__":` block

In the starter or solution file, add a small demo:

1. Build a path to `appsettings.json` in the **subfolder appsettings** in the same folder as the script.
   - Example using `__file__` and `Path(__file__).parent`
2. Call `load_config(config_path)`.
3. Print the resulting `AppConfig` or catch `ConfigError` and print a friendly error.

Example structure (simplified):

```python
if __name__ == "__main__":
    config_path = Path(__file__).parent / "appsettings" / "appsettings.json"
    try:
        config = load_config(config_path)
    except ConfigError as exc:
        print(f"Failed to load config: {exc}")
    else:
        print("Loaded config:")
        print(config)
```

Docs:

- `if __name__ == "__main__":` pattern → https://docs.python.org/3/library/__main__.html
- `Path` operations → https://docs.python.org/3/library/pathlib.html

---

## Discussion Points

- Compare `AppConfig` dataclass to a C# POCO:
  - Similar idea: a simple data holder with named fields.
- Why raise exceptions vs returning `None` or error codes?
  - Clearer control flow, errors can’t be silently ignored.
- Python style:
  - `snake_case` for functions and variables (`load_config`, `retry_count`)
  - Type hints for readability and tooling support
  - Docstrings to describe behavior and expectations

PEP 8 style guide:  
https://peps.python.org/pep-0008/

---

## Stretch Goals

- Add optional settings with sensible defaults, for example:
  - `debug_mode: bool = False`
  - `timeout_seconds: float = 3.0`
- Validate that:
  - `environment` is one of: `"dev"`, `"test"`, `"prod"`
  - `log_level` is one of common log levels.
- Add more detailed error messages naming:
  - Which keys are missing
  - Which values are invalid and why

---

By completing this exercise, you practice:

- Reading JSON config files
- Validating input early and failing fast
- Using dataclasses to represent structured configuration
- Writing small, reusable helper functions with clear responsibilities
