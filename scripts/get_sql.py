import pandas as pd

def get_sql():
    query = """
        SELECT cwd.id AS id, 
        cwd.city_name AS city, 
        date(cwd.timestamp) as utc_date,
        hour(cwd.timestamp) as utc_hour,
        cwd.avg(temperature) AS avg_temperature,
        avg(pressure) AS avg_pressure,
        avg(humidity) AS avg_humidity
        FROM analytics.city_weather_data AS cwd
        GROUP BY cwd.city_name, date(cwd.timestamp),hour(timestamp);
        """
    df = pd.read_sql(query)

