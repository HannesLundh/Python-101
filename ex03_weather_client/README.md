# Exercise 03 – HTTP API Client (Real Weather API)

**Goal:**  
Learn how to call real external HTTP APIs in Python using `requests`, handle errors correctly, and map responses into dataclasses.

This exercise uses real-world services:

- **OpenStreetMap Nominatim** – converts city names into latitude/longitude
- **MET Norway Weather API (Locationforecast/2.0)** – retrieves real weather data

You will learn:

- How to perform HTTP requests
- How to parse and validate JSON
- How to work with exceptions
- How to use dataclasses
- How to compose multiple API calls
- How to structure a simple Python client class

---

# 🔗 Useful Python Documentation (Python 101)

## 📘 Core Docs

- Dataclasses → https://docs.python.org/3/library/dataclasses.html
- Exceptions → https://docs.python.org/3/tutorial/errors.html
- Functions → https://docs.python.org/3/tutorial/controlflow.html#defining-functions
- Imports → https://docs.python.org/3/reference/import.html

## 📦 JSON Handling

- `json` module → https://docs.python.org/3/library/json.html

## 🌐 HTTP Requests

- Requests library → https://requests.readthedocs.io/en/latest/

---

# Files

- `starter_weather_client.py` – starter file with TODOs
- `solution_weather_client.py` – reference solution

---

# Scenario

When a user writes:

```python
client.get_weather("Stockholm")
```

Your job is to:

1. Convert `"Stockholm"` into latitude/longitude using **Nominatim**
2. Fetch weather data for those coordinates from **MET Norway**
3. Return a structured dataclass containing:
   - city name (pretty label)
   - temperature (C°)
   - weather summary text

Example output:

```python
WeatherInfo(
    city="Stockholm, Sverige",
    temperature_c=5.7,
    summary="Partly cloudy"
)
```

---

# API Details

## 1. Geocoding — Nominatim

Endpoint:

```
https://nominatim.openstreetmap.org/search
```

Example query:

```
?q=Stockholm&format=jsonv2&limit=1
```

Response format:

```json
[
  {
    "lat": "59.3293235",
    "lon": "18.0685808",
    "display_name": "Stockholm, Stockholms kommun, Sverige"
  }
]
```

---

## 2. Weather — MET Norway

Endpoint:

```
https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=59.33&lon=18.07
```

Example JSON fragment:

```json
{
  "properties": {
    "timeseries": [
      {
        "data": {
          "instant": {
            "details": {
              "air_temperature": 5.7
            }
          },
          "next_1_hours": {
            "summary": {
              "symbol_code": "partlycloudy_day"
            }
          }
        }
      }
    ]
  }
}
```

---

# Your Tasks

## 1️⃣ Implement `_handle_response(self, response)`

Requirements:

- Raise `ApiClientError` for any non‑2xx response
- Parse JSON using `response.json()`
- Wrap JSON errors in `ApiClientError`
- Return a **dict**

Python docs:  
https://docs.python.org/3/library/json.html  
https://docs.python.org/3/tutorial/errors.html

---

## 2️⃣ Implement `_geocode_city(city)`

Steps:

1. Call Nominatim with:
   - `format=jsonv2`
   - `limit=1`
   - `addressdetails=1`
2. Extract:
   - latitude
   - longitude
   - display_name
3. Validate:
   - Network errors
   - Empty result list
   - Missing keys

Return: `(lat, lon, display_name)`

---

## 3️⃣ Implement `get_weather(self, city: str)`

Steps:

1. Geocode the city → `lat`, `lon`, `display_name`
2. Build MET URL:
   ```
   f"{base_url}/compact"
   ```
3. Call MET with:
   - `lat`
   - `lon`
   - headers containing `User-Agent`
4. Parse the JSON using `_handle_response`
5. Extract:
   - temperature
   - first available symbol_code in:
     - `next_1_hours`
     - `next_6_hours`
     - `next_12_hours`
6. Convert symbol_code to human text
7. Return `WeatherInfo(city, temperature_c, summary)`

---

# Demo (main)

```python
client = WeatherClient(
    base_url="https://api.met.no/weatherapi/locationforecast/2.0",
    user_agent="example-weather-client/0.1 your-email@example.com"
)

info = client.get_weather("Stockholm, Sweden")
print(info)
```

---

# Discussion Topics

### Error Handling

- Should API failures raise exceptions or return fallback values?

### Dataclasses

- Why use them instead of writing a normal class?

### Working with Real APIs

- Network latency
- Rate limits
- Required headers
- Changing API schemas

---

# Stretch Goals

- Implement `get_many_cities([...])`
- Add retry logic
- Cache coordinates locally
- Build an async version with `aiohttp`

---

# You're ready!

This is a real-world workflow:  
**input → geocode → weather → dataclass → return to user**.
