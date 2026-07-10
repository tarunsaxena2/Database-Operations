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

query = """
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    student_name VARCHAR(100),
    student_email VARCHAR(100),
    student_course VARCHAR(100)
)
"""

cursor.execute(query)

connection.commit()

print("Students table created successfully")

cursor.close()
connection.close()