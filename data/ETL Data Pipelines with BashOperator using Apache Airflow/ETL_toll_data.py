# Import libraries
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

#defining DAG arguments
# Task 1.1 - defining DAG arguments
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(0),
    'email': ['airflow@example.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}


# defining the DAG
# Task 1.2 - defining the DAG
dag = DAG(
    'ETL_toll_data',
    schedule_interval=timedelta(days=1),
    default_args=default_args,
    description='Apache Airflow Final Assignment',
)


# define the tasks
# Task 1.3 unziping tolldata.tgz
unzip_data = BashOperator(
    task_id='unzip_data',
    bash_command='tar -xzf /home/project/airflow/dags/finalassignment/tolldata.tgz -C /home/project/airflow/dags/finalassignment',
    dag=dag,
)


# Task 1.4 - Create a task to extract data from csv file
extract_data_from_csv = BashOperator(
    task_id = 'extract_data_from_csv',
    bash_command = 'cut -d "," -f1-4 /home/project/airflow/dags/finalassignment/vehicle-data.csv > /home/project/airflow/dags/finalassignment/csv_data.csv',
    dag = dag,
)

# Task 1.5 - Create a task to extract data from tsv file
extract_data_from_tsv= BashOperator(
    task_id = 'extract_data_from_tsv',
    bash_command = 'cut -f5-7 /home/project/airflow/dags/finalassignment/tollplaza-data.tsv | tr "\t" "," > /home/project/airflow/dags/finalassignment/tsv_data.csv',
    dag = dag,
)
# Task 1.6 - Create a task to extract data from fixed width file
extract_data_from_fixed_width = BashOperator(
    task_id = 'extract_data_from_fixed_width',
    bash_command = 'cut -c 59- /home/project/airflow/dags/finalassignment/payment-data.txt | tr " " "," > /home/project/airflow/dags/finalassignment/fixed_width_data.csv',
    dag = dag,
)

# Task 1.7 - Create a task to consolidate data extracted from previous tasks
consolidate_data = BashOperator(
    task_id = 'consolidate_data',
    bash_command = 'paste -d "," /home/project/airflow/dags/finalassignment/csv_data.csv \
    /home/project/airflow/dags/finalassignment/tsv_data.csv \
    /home/project/airflow/dags/finalassignment/fixed_width_data.csv \
    > /home/project/airflow/dags/finalassignment/extracted_data.csv',
    dag = dag,
)

#Task 1.8 -Transform and load the data
transform_data = BashOperator(
    task_id = 'transform_data',
    bash_command = r"sed 's/[^,]*/\U&/4' /home/project/airflow/dags/finalassignment/extracted_data.csv > /home/project/airflow/dags/finalassignment/transformed_data.csv",
    dag = dag,
)


# task pipeline
unzip_data >> extract_data_from_csv >> extract_data_from_tsv >> extract_data_from_fixed_width >> consolidate_data >> transform_data