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

student_id = input("Enter Student ID: ")
new_course = input("Enter New Course: ")

query = """
UPDATE students
SET student_course = %s
WHERE student_id = %s
"""

cursor.execute(query, (new_course, student_id))

connection.commit()

print("Student record updated successfully")

cursor.close()
connection.close()