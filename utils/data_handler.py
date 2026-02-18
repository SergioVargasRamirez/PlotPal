import pandas as pd
from io import StringIO

def load_data_from_paste(paste_text: str) -> pd.DataFrame:
    """Load CSV from pasted text."""
    try:
        df = pd.read_csv(StringIO(paste_text))
        return df
    except Exception as e:
        raise ValueError(f"Error parsing data: {e}")

def validate_dataframe(df: pd.DataFrame) -> bool:
    """Check if dataframe is not empty."""
    return not df.empty

def create_empty_dataframe(column_names: list, num_rows: int) -> pd.DataFrame:
    """Return a DataFrame filled with empty strings with given shape."""
    return pd.DataFrame({name: [""]*num_rows for name in column_names})
