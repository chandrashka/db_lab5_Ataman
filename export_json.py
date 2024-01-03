import json
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
track_query = "SELECT * FROM Track;"
artist_query = "SELECT * FROM Artist;"
playlist_query = "SELECT * FROM Playlist;"
charts_query = "SELECT * FROM Charts;"
streams_query = "SELECT * FROM Streams;"

# Отримання даних з кожної таблиці
cursor.execute(track_query)
track_data = cursor.fetchall()

cursor.execute(artist_query)
artist_data = cursor.fetchall()

cursor.execute(playlist_query)
playlist_data = cursor.fetchall()

cursor.execute(charts_query)
charts_data = cursor.fetchall()

cursor.execute(streams_query)
streams_data = cursor.fetchall()

# Закриття з'єднання з базою даних
conn.close()

# Запис даних у JSON-файл
with open('exported_data.json', 'w') as json_file:
    data = {
        'Track': track_data,
        'Artist': artist_data,
        'Playlist': playlist_data,
        'Charts': charts_data,
        'Streams': streams_data
    }
    json.dump(data, json_file, indent=2)
