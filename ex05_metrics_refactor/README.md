# Exercise 05 – Refactor to Pythonic Code + Tests

**Goal:**  
Take a messy script and refactor it into clean, testable, idiomatic
Python with unit tests.

You’ll practice:

- Using context managers for files
- Working with JSON
- Writing pure functions
- Adding type hints
- Writing unit tests with pytest

---

## 🔗 Useful Python Documentation

### 📘 Core Language & Style

- Python Tutorial → https://docs.python.org/3/tutorial/
- Style guide (PEP 8) → https://peps.python.org/pep-0008/
- Functions & `def` → https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Exceptions & error handling → https://docs.python.org/3/tutorial/errors.html

### 📦 Standard Library Used Here

- `json` (parse JSON files) → https://docs.python.org/3/library/json.html
- `pathlib.Path` (file paths) → https://docs.python.org/3/library/pathlib.html

### 🧾 Typing & Sequences

- Type hints (`typing`) → https://docs.python.org/3/library/typing.html
  - `Sequence` → https://docs.python.org/3/library/typing.html#typing.Sequence
  - `List` → https://docs.python.org/3/library/typing.html#typing.List

### 🧪 Testing

- pytest documentation → https://docs.pytest.org/en/stable/
- `assert` statement in Python → https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement

---

## Files

- `bad_metrics_script.py` – intentionally bad code
- `starter_metrics.py` – skeleton of refactored code
- `starter_test_metrics.py` – skeleton tests
- `solution_metrics.py` – reference solution
- `solution_test_metrics.py` – reference tests

---

## The Bad Script (`bad_metrics_script.py`)

The script:

- Opens file handles manually (`f = open(...); f.close()`).
- Calls `exit(1)` directly.
- Does everything at the top level (no functions).
- Has no type hints.
- Is hard to test.

Your job is to move the logic into **small, testable functions** and then
write tests for those functions.

---

## Your Tasks

### 1️⃣ Inspect `bad_metrics_script.py`

Notice issues like:

- No functions or reuse
- No error handling beyond `exit(1)`
- No separation of concerns (file reading, parsing, and printing all mixed)

You’ll fix all of this in `starter_metrics.py`.

---

### 2️⃣ Implement in `starter_metrics.py`

#### `load_values(path: Path) -> list[float]`

Responsibilities:

- Open the JSON file using a `with` context manager:

  ```python
  with path.open("r", encoding="utf-8") as f:
      raw = json.load(f)
  ```

- Expect JSON format:

  ```json
  [{ "value": 1.0 }, { "value": 2.5 }]
  ```

- Extract `"value"` from each entry and return a list of `float`.
- Let appropriate exceptions surface (or wrap them if desired):
  - `FileNotFoundError` if the file doesn’t exist
  - `json.JSONDecodeError` if the JSON is invalid
  - `KeyError` or `TypeError` if the structure isn’t as expected

Docs:

- `json` → https://docs.python.org/3/library/json.html
- `pathlib.Path` → https://docs.python.org/3/library/pathlib.html

---

#### `calculate_average(values: Sequence[float]) -> float`

Responsibilities:

- Return the arithmetic mean of the values.
- Decide what to do for an **empty sequence**, e.g.:

  - Raise `ValueError("values must not be empty")`

Example idea:

```python
if not values:
    raise ValueError("values must not be empty")

return sum(values) / len(values)
```

Docs:

- Built-in `sum` → https://docs.python.org/3/library/functions.html#sum
- Exceptions → https://docs.python.org/3/tutorial/errors.html

---

#### `main() -> None`

Responsibilities:

- Determine the path to `metrics.json`, e.g.:

  ```python
  from pathlib import Path

  metrics_path = Path(__file__).parent / "metrics.json"
  ```

- Call `load_values(metrics_path)`.
- Call `calculate_average(values)`.
- Print the result using an f-string, e.g.:

  ```python
  print(f"Average value: {avg:.2f}")
  ```

- Use `try`/`except` to handle errors and print a friendly message instead of using `exit(1)`.

Example structure:

```python
def main() -> None:
    metrics_path = Path(__file__).parent / "metrics.json"
    try:
        values = load_values(metrics_path)
        avg = calculate_average(values)
    except Exception as exc:
        print(f"Failed to calculate metrics: {exc}")
        return

    print(f"Average value: {avg:.2f}")
```

Finally, add the standard entrypoint:

```python
if __name__ == "__main__":
    main()
```

Docs:

- `if __name__ == "__main__":` → https://docs.python.org/3/library/__main__.html

---

### 3️⃣ Implement tests in `starter_test_metrics.py`

Use `pytest` to write small, focused tests.

#### `test_calculate_average_simple`

- Assert that `calculate_average([1, 2, 3]) == 2.0` using a plain `assert`.

Example:

```python
def test_calculate_average_simple() -> None:
    assert calculate_average([1, 2, 3]) == 2.0
```

#### `test_calculate_average_empty_list`

- Decide on the behavior for an empty list (e.g. raise `ValueError`).
- Assert that behavior using `pytest.raises`.

Example:

```python
import pytest

def test_calculate_average_empty_list() -> None:
    with pytest.raises(ValueError):
        calculate_average([])
```

Docs:

- pytest `raises` → https://docs.pytest.org/en/stable/how-to/assert.html#assertions-about-expected-exceptions

---

### 4️⃣ Run tests

From the project folder, run:

```bash
pytest
```

You should see tests passing once your implementations are correct.

Docs:

- pytest getting started → https://docs.pytest.org/en/stable/getting-started.html

---

## Discussion Points

- **Why test pure functions?**  
  They have no side effects, take inputs and return outputs → very easy to test.

- **Python tests (pytest) vs C# test frameworks:**

  - Less ceremony; use plain functions and `assert`.
  - No need for classes unless you want them.

- **Error handling:**
  - Using exceptions vs return codes.
  - How to surface clear error messages to users.

---

## Stretch Goals

- Implement `calculate_median(values: Sequence[float]) -> float` and tests.
- Validate all values are numeric:
  - Raise a clear error if a value is not `int` / `float`.
- Add CLI arguments (e.g. allow passing the metrics file path via `sys.argv` or `argparse`).

---

By completing this exercise you practice:

- Refactoring messy, script-style code into clean functions
- Using context managers for files
- Handling JSON data safely
- Writing unit tests that validate behavior
- Applying Pythonic style and idioms
