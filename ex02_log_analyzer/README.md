# Exercise 02 – Log Analyzer

**Goal:** Work with text, parsing, dataclasses, and dictionaries. Build a small
log analyzer that counts log levels (`INFO`, `WARN`, `ERROR`, etc.).

Here are some useful docs to keep handy:

---

## 🔗 Useful Python Documentation

### 📘 Core Concepts

- Strings → https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
- Dataclasses → https://docs.python.org/3/library/dataclasses.html
- Exceptions (for later / stretch) → https://docs.python.org/3/tutorial/errors.html

### 📦 Collections & Iteration

- Dictionaries (`dict`) → https://docs.python.org/3/library/stdtypes.html#mapping-types-dict
- Iteration (`for` loops) → https://docs.python.org/3/tutorial/controlflow.html#for-statements
- Built-in functions → https://docs.python.org/3/library/functions.html

### 💾 Files

- Reading files → https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

---

## Files

- `starter_log_analyzer.py` – starter with TODOs
- `sample.log` – example log file for testing
- `solution_log_analyzer.py` – reference solution

---

## Log Format

Example lines:

```
[INFO] Application started
[ERROR] Something went wrong
[WARN] Low disk space
```

A valid line contains:

- A log level inside square brackets
- A space
- A free-text message

---

## Your Tasks

### 1. `parse_log_line(line: str) -> LogEntry | None`

Implement a parser that:

- Extracts the level between `[` and `]`
- Takes the message as everything after the closing bracket
- Returns `None` if:
  - The line is empty
  - Does not start with `[`
  - The `]` is missing
  - Level/message is empty

Helpful string docs:  
https://docs.python.org/3/library/stdtypes.html#string-methods

---

### 2. `count_by_level(entries: Iterable[LogEntry]) -> Dict[str, int]`

- Takes a list of parsed `LogEntry` objects
- Returns a dictionary mapping levels to counts

Example:

```python
{"INFO": 10, "ERROR": 3}
```

Dict docs:  
https://docs.python.org/3/library/stdtypes.html#mapping-types-dict

---

### 3. `top_n_levels(counts: Dict[str, int], n: int) -> Dict[str, int]`

- Sort levels by count (descending)
- Slice the top `n`
- Return a **new dictionary**

Sorting docs:  
https://docs.python.org/3/howto/sorting.html

---

### 4. Optional `main` function

Add:

1. Read `sample.log`
2. Parse each line
3. Count log levels
4. Print:
   - All counts
   - Top 3 levels

File reading docs:  
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

---

## Discussion Points

- Pure functions → easier testing and fewer side effects
- `dict` vs C# `Dictionary<TKey, TValue>`
- Pythonic iteration:
  ```python
  for entry in entries:
      ...
  ```

---

## Stretch Goals

- Parse timestamps
- Add a function to filter out DEBUG logs
