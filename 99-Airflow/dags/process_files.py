import airflow
from airflow import DAG
from airflow.sensors.http_sensor import HttpSensor
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator

from datetime import datetime, timedelta

import requests

def download_file():
    indata = requests.get('https://raw.githubusercontent.com/tadinve/EKG-Foundations/master/04A-postgress/world.sql')
    with open('/opt/airflow/dags/files/world.sql', 'w') as outfile:
        outfile.write(indata.text)



with DAG(   dag_id="process_files", 
            start_date= airflow.utils.dates.days_ago(1)
        ) as dag:


    start = DummyOperator(
            task_id= "start"
        )

    is_postgres_file_available = HttpSensor(
            task_id="is_postgres_file_available",
            method="GET",
            http_conn_id="http_api",
            endpoint="world.sql",
            response_check=lambda response: "select" in response.text,
            poke_interval=5,
            timeout=20
    )

    download =  PythonOperator(
                task_id = "download",
                python_callable = download_file
    )


    upload_to_pg = PostgresOperator(
                task_id = "upload_to_pg",
                postgres_conn_id = "pg_conn",
                sql = "files/world.sql"

    )

    end = DummyOperator(
            task_id= "end"
        )

    start >> is_postgres_file_available >> download >> upload_to_pg >> end

