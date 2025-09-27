from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class resultClass:
    def __init__(self, root):
        self.root = root
        self.root.title("School Result Management System")
        self.root.geometry("1200x600+80+100")
        self.root.config(bg="white")
        self.root.focus_force()

        self.var_rollno = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_full_marks = StringVar()

        self.rollno_list = []

        title = Label(self.root, text="Add Student Results",
                      font=("goudy old style", 20, "bold"),
                      bg="orange", fg="#262626")
        title.place(x=0, y=15, relwidth=1, height=60)

        Label(self.root, text="Select Student :", font=("goudy old style", 20, 'bold'), bg='white').place(x=50, y=100)
        Label(self.root, text="Name :", font=("goudy old style", 20, 'bold'), bg='white').place(x=50, y=160)
        Label(self.root, text="Course :", font=("goudy old style", 20, 'bold'), bg='white').place(x=50, y=220)
        Label(self.root, text="Marks Obtained :", font=("goudy old style", 20, 'bold'), bg='white').place(x=50, y=280)
        Label(self.root, text="Full Marks :", font=("goudy old style", 20, 'bold'), bg='white').place(x=50, y=340)

        self.txt_student = ttk.Combobox(self.root, textvariable=self.var_rollno,
                                       font=("goudy old style", 15, 'bold'), state='readonly', justify=CENTER)
        self.txt_student.place(x=280, y=100, width=200)
        self.txt_student.set("Select")

        Button(self.root, text='Search', command=self.search_student,
               font=("goudy old style", 15, 'bold'), bg='#03a9f4', fg="white").place(x=500, y=96, width=130, height=40)

        Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, 'bold'), bg='lightyellow', state='readonly').place(x=280, y=160, width=350)
        Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, 'bold'), bg='lightyellow', state='readonly').place(x=280, y=225, width=350)
        Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 20, 'bold'), bg='lightyellow').place(x=280, y=285, width=350)
        Entry(self.root, textvariable=self.var_full_marks, font=("goudy old style", 20, 'bold'), bg='lightyellow').place(x=280, y=345, width=350)

        Button(self.root, text="Submit", command=self.add,
               font=("times new roman", 15), bg="lightgreen", cursor="hand2").place(x=300, y=420, width=120, height=35)
        Button(self.root, text="Clear", command=self.clear_fields,
               font=("times new roman", 15), bg="lightgrey", cursor="hand2").place(x=430, y=420, width=120, height=35)

        try:
            self.bg_image = Image.open("image/Wh.jpg")
            self.bg_image = self.bg_image.resize((700, 450), Image.Resampling.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(self.bg_image)
            self.lbl_bg = Label(self.root, image=self.bg_img)
            self.lbl_bg.place(x=650, y=100, width=700, height=450)
        except Exception as e:
            print("Image load error:", e)



        self.create_result_table()
        self.fetch_rollno()

    def create_result_table(self):
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute('''
                CREATE TABLE IF NOT EXISTS result (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    rollno TEXT,
                    name TEXT,
                    course TEXT,
                    marks_ob TEXT,
                    full_marks TEXT,
                    per TEXT
                )
            ''')
            con.commit()
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error creating table: {str(ex)}", parent=self.root)

    def fetch_rollno(self):
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("SELECT rollno FROM student")
            rows = cur.fetchall()
            self.rollno_list = [row[0] for row in rows]
            self.txt_student['values'] = self.rollno_list
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error fetching roll numbers: {str(ex)}", parent=self.root)

    def search_student(self):
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("SELECT name, course FROM student WHERE rollno = ?", (self.var_rollno.get(),))
            row = cur.fetchone()
            if row:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "Student not found.", parent=self.root)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error searching student: {str(ex)}", parent=self.root)

    def add(self):
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Please search for a student first.", parent=self.root)
                return

            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM result WHERE rollno=? AND course=?", (self.var_rollno.get(), self.var_course.get()))
            row = cur.fetchone()
            if row:
                messagebox.showerror("Error", "Result already exists.", parent=self.root)
            else:
                per = (int(self.var_marks.get()) * 100) / int(self.var_full_marks.get())
                cur.execute("INSERT INTO result (rollno, name, course, marks_ob, full_marks, per) VALUES (?, ?, ?, ?, ?, ?)", (
                    self.var_rollno.get(),
                    self.var_name.get(),
                    self.var_course.get(),
                    self.var_marks.get(),
                    self.var_full_marks.get(),
                    str(round(per, 2))
                ))
                con.commit()
                messagebox.showinfo("Success", "Result added successfully!", parent=self.root)
            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Submission failed: {str(ex)}", parent=self.root)

    def clear_fields(self):
        self.var_rollno.set("Select")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_full_marks.set("")

if __name__ == "__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()