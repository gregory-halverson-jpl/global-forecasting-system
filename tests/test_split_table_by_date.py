import pandas as pd
from datetime import datetime
from global_forecasting_system.global_forecasting_system import split_table_by_date

def test_split_table_by_date():
    # Create a mock DataFrame
    data = {
        "forecast_time_UTC": [
            "2026-01-12 00:00:00",
            "2026-01-12 06:00:00",
            "2026-01-12 12:00:00",
            "2026-01-12 18:00:00",
            "2026-01-13 00:00:00",
        ],
        "value": [1, 2, 3, 4, 5],
    }
    listing = pd.DataFrame(data)
    listing["forecast_time_UTC"] = pd.to_datetime(listing["forecast_time_UTC"])

    # Define the cutoff datetime
    time_UTC = datetime(2026, 1, 12, 12, 0, 0)

    # Call the function
    before_rows, after_rows = split_table_by_date(listing, time_UTC)

    # Assertions
    assert len(before_rows) == 3, f"Expected 3 rows before, got {len(before_rows)}"
    assert len(after_rows) == 2, f"Expected 2 rows after, got {len(after_rows)}"

    assert before_rows.iloc[-1]["forecast_time_UTC"] == pd.Timestamp("2026-01-12 12:00:00"), "Last 'before' row mismatch"
    assert after_rows.iloc[0]["forecast_time_UTC"] == pd.Timestamp("2026-01-12 18:00:00"), "First 'after' row mismatch"

    print("All tests passed!")

if __name__ == "__main__":
    test_split_table_by_date()