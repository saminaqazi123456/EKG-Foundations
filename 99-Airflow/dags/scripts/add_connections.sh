airflow connections delete 'conn_api'
airflow connections delete 'pg_conn'


airflow connections add 'conn_api' --conn-type 'http' --conn-host 'raw.githubusercontent.com/tadinve/EKG-Foundations/master/04A-postgress/'


airflow connections add pg_conn \
  --conn-type 'postgres' \
  --conn-host 'ekg-foundations-postgres-1' \
  --conn-login 'airflow' \
  --conn-password 'airflow' 
