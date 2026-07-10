import psycopg2
import config

connection = psycopg2.connect(
    host=config.db_host,
    database=config.db_name,
    user=config.db_user,
    password=config.db_password,
    port=config.db_port
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("\nStudent Records\n")

for student in students:
    print(student)

cursor.close()
connection.close()