import matplotlib.pyplot as plt
import pandas as pd
import requests

URL = "https://api.open-meteo.com/v1/forecast"
PARAMS = {"latitude": 55.75, "longitude": 37.61, "hourly": "temperature_2m"}


def build_dataframe(hours: list[str], temperatures: list[float]) -> pd.DataFrame:
    """Create a time-sorted temperature DataFrame from local input data."""
    dataframe = pd.DataFrame(
        {"time": pd.to_datetime(hours), "temperature_c": temperatures}
    )
    return dataframe.sort_values("time").reset_index(drop=True)


def main() -> None:
    response = requests.get(URL, params=PARAMS, timeout=10)
    response.raise_for_status()
    data = response.json()

    hours = data["hourly"]["time"][:24]
    temperatures = data["hourly"]["temperature_2m"][:24]
    dataframe = build_dataframe(hours, temperatures)
    dataframe.to_csv("temperature_24h.csv", index=False)

    plt.plot(dataframe["time"], dataframe["temperature_c"], marker="o")
    plt.xticks(rotation=45)
    plt.title("Температура в Москве (24 часа)")
    plt.xlabel("Время")
    plt.ylabel("°C")
    plt.tight_layout()
    plt.savefig("temperature_24h.png")
    plt.close()

    print("Сохранено в temperature_24h.csv и temperature_24h.png")


if __name__ == "__main__":
    main()
