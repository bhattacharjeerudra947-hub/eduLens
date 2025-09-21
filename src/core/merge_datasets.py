import pymysql
import csv

def genera_data_insertion():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="newpassword",
        database="student_data"
    )

    cursor = db.cursor()

    query = "CREATE TABLE IF NOT EXISTS " \
    "students(admn_no int primary key, name varchar(100), class int(2), " \
    "stream varchar(20), student_contact varchar(15), guardian_contact varchar(15), " \
    "guardian_email varchar(200))"
    cursor.execute(query)

    db.commit()

    with open(r"src\datasets\fake_students.csv", "r") as file:

        reader = csv.reader(file)

        next(reader)
        for row in reader:

            q = "insert into students values(%s, %s, %s, %s, %s, %s, %s)"
            v = (row[0], row[1], row[2], row[3], str(row[4]), str(row[5]), row[6])
            cursor.execute(q, v)

    db.commit()
    cursor.close()

def attendance_data_insertion():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="newpassword",
        database="student_data"
    )

    cursor = db.cursor()

    query = "CREATE TABLE IF NOT EXISTS attendance(admn_no int primary key, " \
    "month_1 int, month_2 int, month_3 int, month_4 int, month_5 int, " \
    "month_6 int)"
    cursor.execute(query)

    db.commit()

    with open(r"src\datasets\attendance.csv", "r") as file:

        reader = csv.reader(file)

        next(reader)
        for row in reader:

            q = "insert into attendance values(%s, %s, %s, %s, %s, %s, %s)"
            v = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            cursor.execute(q, v)

        db.commit()
        cursor.close()

def marks_data_insertion():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="newpassword",
        database="student_data"
    )

    cursor = db.cursor()

    query = "CREATE TABLE IF NOT EXISTS marks(admn_no int, " \
    "subject varchar(10), pt_1 int, pt_2 int, mid_term int, total int)"
    cursor.execute(query)

    db.commit()

    with open(r"src\datasets\marks.csv", "r") as file:

        reader = csv.reader(file)

        next(reader)
        for row in reader:

            q = "insert into marks values(%s, %s, %s, %s, %s, %s)"
            v = (row[0], row[1], row[2], row[3], row[4], row[5])
            cursor.execute(q, v)

        db.commit()
        cursor.close()

def merge_tables():

    db = pymysql.connect(
        host="localhost",
        user="root",
        password="newpassword",
        database="student_data"
    )

    cursor = db.cursor()

    query = "CREATE TABLE IF NOT EXISTS student_details AS SELECT" \
    "admn_no, name, class, stream, month_1, month_2, month_3, month_4, " \
    "month_5, month_6 FROM students NATURAL JOIN attendance"

    cursor.execute(query)

    db.commit()
    cursor.close()

if __name__ == "__main__":
    marks_data_insertion()