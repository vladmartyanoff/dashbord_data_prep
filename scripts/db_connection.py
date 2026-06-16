from sqlalchemy import create_engine
from config.db_info import clickhouse_db_url

# Задаем подключение к базе данных
db_url = clickhouse_db_url
def conenct_to_db():
    engine = create_engine(db_url)