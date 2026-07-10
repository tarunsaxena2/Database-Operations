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

student_name = input("Enter student name: ")
student_email = input("Enter student email: ")
student_course = input("Enter student course: ")

query = """
INSERT INTO students
(student_name, student_email, student_course)
VALUES (%s, %s, %s)
"""

cursor.execute(
    query,
    (student_name, student_email, student_course)
)

connection.commit()

print("Student record inserted successfully")

cursor.close()
connection.close()