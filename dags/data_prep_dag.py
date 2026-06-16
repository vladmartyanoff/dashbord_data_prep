from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator



default_args = {
    "owner": "etl_user",
    "depends_on_past": False,
    "start_date": datetime(2026, 6, 15),
    'on_failure_callback': lambda context: print(f"Ошибка миграции: {context['exception']}"),
    "retries": 2,
    "retry_delay": timedelta(minutes=5)
}
with DAG(
    dag_id='dashboard_weather_data_preparation',
    default_args=default_args,
    schedule='55 23 * * *',
    catchup=False,
    max_active_tasks=3,
    max_active_runs=1,
    tags=["weather", "dashboard", "data_preparation"],
    description="Preparing weather data for dashbords",
) as dag:

    db_connection = PythonOperator(
        task_id="db_connection",
        python_callable=connect_to_db,
        dag=dag
    )

    sql_query = PythonOperator(
        task_id="sql_query",
        python_callalble=get_sql,
        dag=dag
    )

    timezone_converting = PythonOperator(
        task_id="timezone_converting",
        python_callalble=timezone_convert,
        dag=dag
    )