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

student_id = input("Enter Student ID to Delete: ")

query = "DELETE FROM students WHERE student_id = %s"

cursor.execute(query, (student_id,))

connection.commit()

print("Student record deleted successfully")

cursor.close()
connection.close()