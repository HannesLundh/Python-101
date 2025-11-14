# Exercise 06 – Python Azure Function (HTTP Trigger)

**Goal:**  
Create a simple **HTTP-triggered Azure Function** in Python and run it locally.  
Compare it with C# Functions and get comfortable with Python + HTTP + JSON.

You’ll practice:

- Handling HTTP requests in Python
- Parsing query parameters and JSON bodies
- Returning JSON responses
- Using environment variables and basic validation

---

## 🔗 Useful Documentation

### 🧵 Azure Functions (Python)

- Azure Functions (Python) docs → https://learn.microsoft.com/azure/azure-functions/functions-reference-python
- HTTP trigger & bindings → https://learn.microsoft.com/azure/azure-functions/functions-bindings-http-webhook-trigger
- Azure Functions Core Tools → https://learn.microsoft.com/azure/azure-functions/functions-core-tools-reference

### 📘 Core Python

- `logging` → https://docs.python.org/3/library/logging.html
- `datetime` (for timestamps) → https://docs.python.org/3/library/datetime.html
- `json` (encode/decode JSON) → https://docs.python.org/3/library/json.html
- `os` & environment variables → https://docs.python.org/3/library/os.html#os.environ

---

## Prerequisites

- Python 3.10+
- Azure Functions Core Tools
- (Recommended) VS Code with Azure Functions extension

---

## Steps

### 1. Create a New Function App

From this `ex06_azure_function_http` folder, run:

```bash
func init PythonHttpDemo --python
cd PythonHttpDemo
func new --name HelloFunction --template "HTTP trigger"
```

Open the **PythonHttpDemo** folder in VS Code.

---

### 2. Inspect the Generated Function

Open:

```text
HelloFunction/__init__.py
```

Replace its contents with the starter below **or** apply the TODOs to the generated file:

```python
import logging
from datetime import datetime

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP-triggered Azure Function that returns a greeting.

    TODOs:
      - Extract "name" from query string OR JSON body.
      - If name is missing, return 400 with an error JSON.
      - If name is present, return:
          {
            "greeting": "Hello <name>!",
            "timestamp": "<iso8601-utc>"
          }
      - Use proper content type (application/json).
    """
    logging.info("HelloFunction processed a request.")

    # TODO: get 'name' from query params
    name = req.params.get("name")

    # TODO: if not present, try to read from JSON body
    if not name:
        try:
            body = req.get_json()
        except ValueError:
            body = {}
        name = body.get("name")

    if not name:
        # TODO: return 400 with JSON error
        return func.HttpResponse(
            body='{"error": "Please provide a \"name\"."}',
            status_code=400,
            mimetype="application/json",
        )

    response_data = {
        "greeting": f"Hello {name}!",
        "timestamp": datetime.utcnow().isoformat(),
    }

    # TODO: serialize response_data as JSON (e.g. using json.dumps)
    import json
    return func.HttpResponse(
        body=json.dumps(response_data),
        status_code=200,
        mimetype="application/json",
    )
```

---

### 3. Run the Function Locally

From inside **PythonHttpDemo**:

```bash
func start
```

You should see a URL similar to:

```text
http://localhost:7071/api/HelloFunction
```

---

### 4. Test the Function

#### Via Browser (query string)

```text
http://localhost:7071/api/HelloFunction?name=Alice
```

#### Via curl (JSON body)

```bash
curl -X POST   http://localhost:7071/api/HelloFunction   -H "Content-Type: application/json"   -d '{"name": "Bob"}'
```

**Expected response (example):**

```json
{
  "greeting": "Hello Bob!",
  "timestamp": "2025-11-13T09:32:10.123456"
}
```

---

## Discussion Points

- Differences vs C# Azure Functions bindings:
  - No method overloading, dynamic typing, etc.
- Request/response types:
  - `func.HttpRequest` for incoming HTTP requests
  - `func.HttpResponse` for outgoing responses
- Where Python feels more dynamic vs static C#:
  - Less ceremony for JSON handling
  - Easier experimentation in local dev

---

## Stretch Goals

- Read a `DEFAULT_NAME` from `local.settings.json` / environment if no name is provided
- Add simple validation (e.g., reject numeric-only or digit-containing names)
- Add another function:
  - `/health` returning `{ "status": "ok" }`
- Log extra metadata:
  - Query params
  - Client IP
  - Request method

---

By completing this exercise you will:

- Understand how Python Azure Functions handle HTTP requests
- Practice combining query string parsing, JSON parsing, and environment variables
- See how Python compares to C# in the Azure Functions world
