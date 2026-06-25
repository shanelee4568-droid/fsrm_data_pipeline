import polars as pl
import pytest
from pathlib import Path

from pipeline.load import check_duplicate_dates, check_and_load_to_backup

@pytest.fixture
def base_df() -> pl.DataFrame:
    return pl.DataFrame({
        "stock_date": ["2026-06-20", "2026-06-21"],
        "price": [100.5, 102.0]
    })


@pytest.fixture
def new_df_overlap() -> pl.DataFrame:
    return pl.DataFrame({
        "stock_date": ["2026-06-21", "2026-06-22"],
        "price": [102.0, 105.5]
    })


@pytest.fixture
def new_df_clean() -> pl.DataFrame:
    return pl.DataFrame({
        "stock_date": ["2026-06-22", "2026-06-23"],
        "price": [105.5, 107.0]
    })