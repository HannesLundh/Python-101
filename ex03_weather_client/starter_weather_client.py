from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional
import requests


class ApiClientError(Exception):
    """Raised when HTTP call fails or returns an unexpected response."""


@dataclass
class WeatherInfo:
    """Simple container for the data our client returns to callers."""
    city: str
    temperature_c: float
    summary: str


class WeatherClient:
    """
    HTTP client for a real weather workflow.

    This version will eventually do TWO HTTP calls:

      1. Geocoding: city name -> latitude/longitude (Nominatim)
      2. Weather:  coordinates -> weather data (MET Norway Locationforecast)

    You will implement the missing pieces step by step.
    """

    def __init__(
        self,
        base_url: str,
        timeout_seconds: float = 3.0,
        user_agent: Optional[str] = None,
    ) -> None:
        """
        base_url:
            Base URL for the MET API, for example:
                "https://api.met.no/weatherapi/locationforecast/2.0"

        timeout_seconds:
            HTTP timeout for *all* requests.

        user_agent:
            Required by both Nominatim and MET. Must identify your app and
            contain some way to contact you (e.g. email or URL).
        """
        self._base_url = base_url.rstrip("/")
        self._timeout_seconds = timeout_seconds
        self._user_agent = (
            user_agent or "example-weather-client/0.1 your-contact@example.com"
        )

    # ------------------------------------------------------------------
    # Shared HTTP response helper
    # ------------------------------------------------------------------
    def _handle_response(self, response: requests.Response) -> Dict[str, Any]:
        """
        Handle a raw HTTP response.

        TODO:
          - If response.ok is False (non-2xx status), raise ApiClientError.
          - Parse the body as JSON: response.json().
          - If JSON parsing fails (ValueError), wrap it in ApiClientError.
          - Return the parsed JSON (as a dict).

        NOTE: For this exercise you can assume the root JSON value is an object
        (dict), not a list.
        """
        raise NotImplementedError("_handle_response is not implemented yet")

    # ------------------------------------------------------------------
    # Geocoding helper (city -> coordinates)
    # ------------------------------------------------------------------
    def _geocode_city(self, city: str) -> tuple[float, float, str]:
        """
        Convert a city name into (lat, lon, display_name) using Nominatim.

        API docs:
          - https://nominatim.org/release-docs/latest/api/Search/

        You should:

          - Call: https://nominatim.openstreetmap.org/search
          - Use query parameters:
                q=city
                format=jsonv2
                limit=1
                addressdetails=1
          - Send a proper User-Agent header (self._user_agent).
          - Handle network errors (requests.RequestException) and wrap them
            in ApiClientError.
          - Parse the JSON response. It will be a list of results. Use the
            FIRST result (index 0).
          - Extract lat and lon (strings in the JSON). Convert them to float.
          - Extract display_name (fall back to the original city name if it is
            missing).
          - If there are no results, raise ApiClientError.

        Return:
          (latitude, longitude, display_name)
        """
        raise NotImplementedError("_geocode_city is not implemented yet")

    # ------------------------------------------------------------------
    # (Optional) helper: convert MET symbol_code to human text
    # ------------------------------------------------------------------
    @staticmethod
    def _symbol_to_text(symbol_code: str) -> str:
        """
        Convert a MET "symbol_code" (e.g. "partlycloudy_day") to
        something more readable (e.g. "Partly cloudy").

        This helper is mostly to keep get_weather() cleaner.
        You can start simple, for example:

            - Replace "_day" / "_night"
            - Replace "_" with space
            - Capitalize the result

        Stretch goal: add a dict with nicer phrases for common codes.
        """
        # Simple default implementation you can improve later:
        text = (
            symbol_code.replace("_day", "")
            .replace("_night", "")
            .replace("_", " ")
        )
        return text.capitalize()

    # ------------------------------------------------------------------
    # Public API: city -> WeatherInfo
    # ------------------------------------------------------------------
    def get_weather(self, city: str) -> WeatherInfo:
        """
        Retrieve weather info for a single city.

        High-level flow:

          1. Geocode the city name to coordinates:
               lat, lon, display_name = self._geocode_city(city)

          2. Call MET Norway's Locationforecast API (compact endpoint):
               URL:  f"{self._base_url}/compact"
               Query parameters:
                   lat = rounded latitude (e.g. round(lat, 4))
                   lon = rounded longitude
               Headers:
                   User-Agent = self._user_agent
                   Accept     = "application/json"

               Use requests.get(..., timeout=self._timeout_seconds).

          3. Use self._handle_response(...) to parse the JSON body.

          4. From the JSON, extract:
               - Temperature (Celsius) from:
                   properties.timeseries[0].data.instant.details.air_temperature

               - A weather summary from the first available block in:
                   next_1_hours.summary.symbol_code
                   next_6_hours.summary.symbol_code
                   next_12_hours.summary.symbol_code

                 If you find a symbol_code, turn it into text using
                 self._symbol_to_text(symbol_code). If none are found,
                 you can fall back to something like "No summary available".

          5. Return a WeatherInfo instance with:
               city          = display_name from the geocoder
               temperature_c = the parsed air_temperature (float)
               summary       = your human-readable summary string

        Error handling:

          - Network errors (requests.RequestException) should be caught and
            wrapped in ApiClientError.
          - If expected keys are missing in the JSON, wrap KeyError in
            ApiClientError with a helpful message.
          - If numeric conversions fail, wrap TypeError/ValueError similarly.
        """
        raise NotImplementedError("get_weather is not implemented yet")


def main() -> None:
    """
    Simple manual test.

    You now have a real end-to-end flow:

      city name -> Nominatim (geocoding) -> MET (weather)

    This will make real HTTP requests, so you need an internet connection,
    and you should use your own descriptive User-Agent string.
    """
    base_url = "https://api.met.no/weatherapi/locationforecast/2.0"
    client = WeatherClient(
        base_url=base_url,
        timeout_seconds=5.0,
        user_agent="example-weather-client/0.1 your-contact@example.com",
    )

    city = "Stockholm, Sweden"
    try:
        info = client.get_weather(city)
        print(f"Weather in {info.city}: {info.temperature_c:.1f}°C, {info.summary}")
    except ApiClientError as exc:
        print(f"API client error: {exc}")


if __name__ == "__main__":
    main()
