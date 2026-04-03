import sqlite3
import os

def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE STUDENTS (
    id INTEGER PRIMARY KEY,
    name VARCHAR(255),
    age INTEGER,
    email VARCHAR(255) UNIQUE NOT NULL,
    city VARCHAR    
    )
    ''')

    cursor.execute('''
        CREATE TABLE Courses (
        id INTEGER PRIMARY KEY,
        course_name VARCHAR(255) NOT NULL,
        instructor TEXT,
        credits INTEGER 
        )
        ''')

def insert_sample_data(cursor):
    student = [
        (1, 'halit bektas', 22, 'halit@gmail.com', 'istanbul'),
        (2, 'enes kocyigit', 19, 'enes@gmail.com', 'cankiri'),
        (3, 'c kocyigit', 21, 'c@gmail.com', 'canakkale'),
        (4, 'd kocyigit', 23, 'd@gmail.com', 'balikesir'),
        (5, 'e kocyigit', 24, 'r@gmail.com', 'ankara'),
        (6, 'f kocyigit', 18, 'f@gmail.com', 'mugla'),
    ]

    cursor.executemany("INSERT INTO STUDENTS VALUES (?, ?, ?, ?, ?)", student)

    courses = [
        (1, 'Python Programming', 'Dr. Smith', 4),
        (2, 'Web Development', 'Dr. Johnson', 3),
        (3, 'Data Science', 'Dr. Lee', 4),
        (4, 'Mobile Apps', 'Dr. Brown', 3),
        (5, 'Computer Science', 'Dr. Davis', 4),
    ]

    cursor.executemany("INSERT INTO Courses VALUES (?, ?, ?, ?)", courses)

    print("Sample data inserted successfully.")


def basic_sql_operations(cursor):
    cursor.execute("SELECT * FROM STUDENTS")
    students = cursor.fetchall()
    print("All Students:")
    for student in students:
        print(student[0], student[1], student[2], student[3], student[4])

    print("--------Where Clause--------")
    cursor.execute("SELECT * FROM STUDENTS WHERE age > 20")
    students = cursor.fetchall()
    print("Students older than 20:")
    for student in students:
        print(student[0], student[1], student[2], student[3], student[4])

    print("--------Where With String--------")
    cursor.execute("SELECT * FROM STUDENTS WHERE name LIKE 'h%'")
    students = cursor.fetchall()
    print("Students whose names start with 'h':")
    for student in students:
        print(student[0], student[1], student[2], student[3], student[4])

    print("--------Order By--------")
    cursor.execute("SELECT * FROM STUDENTS ORDER BY age DESC ")
    students = cursor.fetchall()
    print("Students ordered by age descending:")
    for student in students:
        print(student[0], student[1], student[2], student[3], student[4])


def sql_update_delete_insert_operations(conn, cursor):
    cursor.execute("INSERT INTO STUDENTS VALUES (7, 'Frank Miller',24,'frank@gmail.com','New York')")
    conn.commit()

    cursor.execute("UPDATE STUDENTS SET age = 24 WHERE id = 1")
    conn.commit()

    cursor.execute("DELETE FROM STUDENTS WHERE id = 2")
    conn.commit()

def aggregate_functions(cursor):
    cursor.execute("SELECT COUNT(*) FROM STUDENTS")
    result = cursor.fetchone()
    print("Total number of students:", result[0])


    cursor.execute("SELECT AVG(age) FROM STUDENTS")
    result = cursor.fetchone()
    print("Average age of students:", result[0])


def main():
    conn, cursor = create_database()
    try:
        create_tables(cursor)
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        sql_update_delete_insert_operations(conn, cursor)
        aggregate_functions(cursor)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()

if __name__ == "__main__":
    main()