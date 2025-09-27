# create_db.py
import sqlite3

def create_db():
        con=sqlite3.connect(database="rms.db")
        cur = con.cursor()

        # Create course table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS course (
                cid INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                duration TEXT,
                charges TEXT,
                description TEXT
            )
        """)
        con.commit()

        # Create student table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS student (
                rollno INTEGER PRIMARY KEY AUTOINCREMENT,
                Name TEXT NOT NULL,
                email TEXT UNIQUE,
                gender TEXT,
                dob TEXT,
                contact TEXT,
                admission TEXT,
                course TEXT,
                state TEXT,
                city TEXT,
                pin TEXT,
                address TEXT
            )
        """)
        con.commit()

        # Create result table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS result (
                rid INTEGER PRIMARY KEY AUTOINCREMENT,
                rollno TEXT,
                name TEXT,
                course TEXT,
                marks_ob TEXT,
                full_marks TEXT,
                per TEXT
            )
        """)
        con.commit()


        # Create employee (users) table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS employee (
                eid INTEGER PRIMARY KEY AUTOINCREMENT,
                f_name TEXT,
                l_name TEXT,
                contact TEXT,
                email TEXT UNIQUE,
                questions TEXT,
                answer TEXT,
                password TEXT
            )
        """)
        con.commit()

        


create_db()
