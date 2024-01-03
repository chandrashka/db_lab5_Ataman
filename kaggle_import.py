import pandas as pd
from sqlalchemy import create_engine

db_params = {
    'dbname': 'spotify',
    'user': 'ataman',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

# Шлях до CSV-файлу з Kaggle
csv_file_path = 'C:/Users/julia/Downloads/archive/spotify-2023.csv'

table_name = 'new_table'
columns_to_import = ['streams', 'released_day']

# Створення з'єднання з базою даних
engine = create_engine(f'postgresql://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}')

# Імпорт даних з CSV в таблицю PostgreSQL
try:
    # Читання CSV-файлу за допомогою pandas
    df = pd.read_csv(csv_file_path, encoding='cp1251')

    # Обмеження кількості стовпців, які імпортуються
    df = df[columns_to_import]

    # Запис даних в таблицю PostgreSQL
    df.to_sql(table_name, engine, if_exists='replace', index=False)

    print(f"Дані з {csv_file_path} імпортовано успішно у таблицю {table_name} у базі даних {db_params['dbname']}.")
except Exception as e:
    print(f"Помилка імпорту даних: {e}")
finally:
    # Закриття з'єднання з базою даних
    engine.dispose()
