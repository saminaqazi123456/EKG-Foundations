# Three steps up Airflow

- curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.3.3/docker-compose.yaml'
- echo -e "AIRFLOW_UID=$(id -u)" > .env
- docker-compose up 