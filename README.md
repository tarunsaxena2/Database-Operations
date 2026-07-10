# Python Database Operations Assignment

## Student Details

**Name:** Tarun Saxena

---

## Project Description

This project demonstrates basic database operations using Python and PostgreSQL. The programs connect to the database and perform common SQL operations step by step.

The operations included are:

* Create a database
* Create a table
* Insert student records
* Display records
* Update a student record
* Delete a student record
* Display the final records

---

## Project Structure

```
Database-Tarun
│
├── python_files
│   ├── config.py
│   ├── 01_create_database.py
│   ├── 02_create_table.py
│   ├── 03_insert_student.py
│   ├── 04_display_students.py
│   ├── 05_update_student.py
│   ├── 06_delete_student.py
│   └── 07_final_display.py
│
├── screenshots
│
├── requirements.txt
└── README.md
```

---

## Requirements

* Python 3.x
* PostgreSQL
* psycopg2-binary

Install the required package using:

```
pip install psycopg2-binary
```

---

## How to Run

1. Open the project folder in VS Code.
2. Update the database details in `config.py`.
3. Open the terminal.
4. Run each file in sequence:

```
python 01_create_database.py
python 02_create_table.py
python 03_insert_student.py
python 04_display_students.py
python 05_update_student.py
python 06_delete_student.py
python 07_final_display.py
```

---

## Testing

I ran each Python file individually from the terminal and verified that the database operations worked correctly. After running every program, I checked the output and confirmed that the corresponding changes were reflected in the database.

The `screenshots` folder contains terminal screenshots captured while testing each program.

---

## Learning Outcome

Through this assignment, I learned how to:

* Connect Python with PostgreSQL
* Execute SQL queries using Python
* Create databases and tables
* Insert, read, update, and delete records
* Commit database changes
* Close database connections properly
