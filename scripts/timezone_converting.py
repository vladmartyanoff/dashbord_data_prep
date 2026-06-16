from get_sql import df
import pandas as pd

def timezone_convert():
    df['timestamp'] = pd.to_datetime(df['timestamp'], utc=True)
