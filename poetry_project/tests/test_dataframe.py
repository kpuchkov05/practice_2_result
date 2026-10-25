from plt_temp import build_dataframe


def test_build_dataframe_sorts_time_and_preserves_temperatures() -> None:
    hours = ["2026-01-01T02:00", "2026-01-01T00:00", "2026-01-01T01:00"]
    temperatures = [2.5, 0.5, 1.5]

    dataframe = build_dataframe(hours, temperatures)

    assert list(dataframe.columns) == ["time", "temperature_c"]
    assert len(dataframe) == 3
    assert dataframe["time"].dt.strftime("%Y-%m-%dT%H:%M").tolist() == [
        "2026-01-01T00:00",
        "2026-01-01T01:00",
        "2026-01-01T02:00",
    ]
    assert dataframe["temperature_c"].tolist() == [0.5, 1.5, 2.5]
