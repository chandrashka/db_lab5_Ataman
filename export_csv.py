import csv
import psycopg2

# Підключення до бази даних PostgreSQL
conn = psycopg2.connect(
    dbname='spotify', 
    user='ataman',  
    password='postgres',
    host='localhost',
)

cursor = conn.cursor()

# Запити для отримання даних з таблиць
tables = ['Track', 'Artist', 'Playlist', 'Charts', 'Streams']

with open('exported_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for table in tables:
        query = f"SELECT * FROM {table};"
        cursor.execute(query)

        # Перевірка, чи є результати запиту
        if cursor.description:
            writer.writerow([desc[0] for desc in cursor.description])
            writer.writerows(cursor.fetchall())
        else:
            print(f"No data returned for the {table} table")

# Закриття з'єднання з базою даних
conn.close()