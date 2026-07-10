import psycopg2

database_name = "database_operations"

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="Tarun@0045",
    port="5432"
)

connection.autocommit = True

cursor = connection.cursor()

query = "CREATE DATABASE " + database_name

cursor.execute(query)

print("Database created successfully")

cursor.close()
connection.close()