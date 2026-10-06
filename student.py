from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class studentClass:
    def __init__(self, root):
        self.root = root
        self.root.title("School Result Management System")
        self.root.geometry("1200x600+80+100")
        self.root.config(bg="white")
        self.root.focus_force()

        # ==== Title Label ====
        title = Label(
            self.root,
            text="Manage Student Details",
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white"
        )
        title.place(x=0, y=15, relwidth=1, height=55)

        # ====== Variables ======
        self.var_rollno = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()
        self.var_a_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_search = StringVar()

        # ===== Number Validation =====
        # Isse Roll No, Pin aur Search me sirf number type hoga
        number_cmd = (self.root.register(self.only_numbers), "%P")

        # ===== Widgets =====
        # ============= Column 1 =============
        Label(
            self.root,
            text="Roll No. :",
            font=("goudy old style", 15, 'bold'),
            bg='white'
        ).place(x=10, y=90)

        Label(
            self.root,
            text="Name :",
            font=("goudy old style", 15, 'bold'),
            bg='white'
        ).place(x=10, y=140)

        Label(
            self.root,
            text="Email :",
            font=("goudy old style", 15, 'bold'),
            bg='white'
        ).place(x=10, y=190)

        Label(
            self.root,
            text="Gender :",
            font=("goudy old style", 15, 'bold'),
            bg='white'
        ).place(x=10, y=240)

        Label(
            self.root,
            text="State :",
            font=("goudy old style", 15, 'bold'),
            bg='white'
        ).place(x=10, y=290)

        Label(
            self.root,
            text="City :",
            font=("goudy old style", 15, 'bold'),
            bg='white'
        ).place(x=330, y=290)

        Label(
            self.root,
            text="Pin :",
            font=("goudy old style", 15, 'bold'),
            bg='white'
        ).place(x=590, y=290)

        Label(
            self.root,
            text="Address :",
            font=("goudy old style", 15, 'bold'),
            bg='white'
        ).place(x=10, y=340)

        # Roll No - only numbers
        self.txt_rollno = Entry(
            self.root,
            textvariable=self.var_rollno,
            font=("goudy old style", 15, 'bold'),
            bg='lightyellow',
            validate="key",
            validatecommand=number_cmd
        )
        self.txt_rollno.place(x=150, y=90, width=200)

        self.txt_name = Entry(
            self.root,
            textvariable=self.var_name,
            font=("goudy old style", 15, 'bold'),
            bg='lightyellow'
        )
        self.txt_name.place(x=150, y=140, width=200)

        self.txt_email = Entry(
            self.root,
            textvariable=self.var_email,
            font=("goudy old style", 15, 'bold'),
            bg='lightyellow'
        )
        self.txt_email.place(x=150, y=190, width=200)

        self.txt_gender = ttk.Combobox(
            self.root,
            textvariable=self.var_gender,
            values=("Select", "Male", "Female", "Other"),
            font=("goudy old style", 15, 'bold'),
            state='readonly',
            justify=CENTER
        )
        self.txt_gender.place(x=150, y=240, width=200)
        self.txt_gender.current(0)

        self.txt_state = Entry(
            self.root,
            textvariable=self.var_state,
            font=("goudy old style", 15, 'bold'),
            bg='lightyellow'
        )
        self.txt_state.place(x=150, y=295, width=150)

        self.txt_city = Entry(
            self.root,
            textvariable=self.var_city,
            font=("goudy old style", 15, 'bold'),
            bg='lightyellow'
        )
        self.txt_city.place(x=410, y=295, width=120)

        # Pin - only numbers
        self.txt_pin = Entry(
            self.root,
            textvariable=self.var_pin,
            font=("goudy old style", 15, 'bold'),
            bg='lightyellow',
            validate="key",
            validatecommand=number_cmd
        )
        self.txt_pin.place(x=680, y=295, width=150)

        self.txt_address = Text(
            self.root,
            font=("goudy old style", 15, 'bold'),
            bg='lightyellow'
        )
        self.txt_address.place(x=150, y=340, width=700, height=150)

        # Column 2
        Label(
            self.root,
            text="D.O.B. :",
            font=("goudy old style", 15, 'bold'),
            bg='white'
        ).place(x=390, y=90)

        Label(
            self.root,
            text="Contact :",
            font=("goudy old style", 15, 'bold'),
            bg='white'
        ).place(x=390, y=140)

        Label(
            self.root,
            text="Admission :",
            font=("goudy old style", 15, 'bold'),
            bg='white'
        ).place(x=390, y=190)

        Label(
            self.root,
            text="Course :",
            font=("goudy old style", 15, 'bold'),
            bg='white'
        ).place(x=390, y=240)

        self.course_list = []

        self.txt_dob = Entry(
            self.root,
            textvariable=self.var_dob,
            font=("goudy old style", 15, 'bold'),
            bg='lightyellow'
        )
        self.txt_dob.place(x=530, y=90, width=200)

        self.txt_contact = Entry(
            self.root,
            textvariable=self.var_contact,
            font=("goudy old style", 15, 'bold'),
            bg='lightyellow'
        )
        self.txt_contact.place(x=530, y=140, width=200)

        self.txt_admission = Entry(
            self.root,
            textvariable=self.var_a_date,
            font=("goudy old style", 15, 'bold'),
            bg='lightyellow'
        )
        self.txt_admission.place(x=530, y=190, width=200)

        self.txt_course = ttk.Combobox(
            self.root,
            textvariable=self.var_course,
            values=self.course_list,
            font=("goudy old style", 15, 'bold'),
            state='readonly',
            justify=CENTER
        )
        self.txt_course.place(x=530, y=240, width=200)
        self.txt_course.set("Empty")

        # Buttons
        Button(
            self.root,
            text='Save',
            command=self.add,
            font=("goudy old style", 15, 'bold'),
            bg='#2196f3',
            fg="white"
        ).place(x=150, y=520, width=110, height=40)

        Button(
            self.root,
            text='Update',
            command=self.update,
            font=("goudy old style", 15, 'bold'),
            bg='#4caf50',
            fg="white"
        ).place(x=270, y=520, width=110, height=40)

        Button(
            self.root,
            text='Delete',
            command=self.delete,
            font=("goudy old style", 15, 'bold'),
            bg='#f44336',
            fg="white"
        ).place(x=390, y=520, width=110, height=40)

        Button(
            self.root,
            text='Clear',
            command=self.clear,
            font=("goudy old style", 15, 'bold'),
            bg='#607d8b',
            fg="white"
        ).place(x=510, y=520, width=110, height=40)

        # Search Panel
        Label(
            self.root,
            text="Roll No. :",
            font=("goudy old style", 15, 'bold'),
            bg='white'
        ).place(x=940, y=110)

        # Search Roll No - only numbers
        Entry(
            self.root,
            textvariable=self.var_search,
            font=("goudy old style", 15, 'bold'),
            bg='lightyellow',
            validate="key",
            validatecommand=number_cmd
        ).place(x=1090, y=110, width=220)

        Button(
            self.root,
            text='Search',
            command=self.search,
            font=("goudy old style", 15, 'bold'),
            bg='#03a9f4',
            fg="white"
        ).place(x=1330, y=100, width=180, height=40)

        # Table
        self.C_Frame = Frame(self.root, bd=2, relief=RIDGE)
        self.C_Frame.place(x=920, y=200, width=600, height=550)

        scrollx = Scrollbar(self.C_Frame, orient=HORIZONTAL)
        scrolly = Scrollbar(self.C_Frame, orient=VERTICAL)

        self.CourseTable = ttk.Treeview(
            self.C_Frame,
            columns=(
                "rollno",
                "Name",
                "email",
                "gender",
                "dob",
                "contact",
                "admission",
                "course",
                "state",
                "city",
                "pin",
                "address"
            ),
            xscrollcommand=scrollx.set,
            yscrollcommand=scrolly.set
        )

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)

        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)

        for col in self.CourseTable["columns"]:
            self.CourseTable.heading(col, text=col.capitalize())
            self.CourseTable.column(col, width=100)

        self.CourseTable["show"] = "headings"
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>", self.get_data)

        self.fetch_course()
        self.show()

    # ===== Change 1: Number validation function added =====
    def only_numbers(self, value):
        if value == "":
            return True
        return value.isdigit()

    def add(self):
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()

            if self.var_rollno.get() == "":
                messagebox.showerror("Error", "Roll No. is required", parent=self.root)
                return

            cur.execute("SELECT * FROM student WHERE rollno=?", (self.var_rollno.get(),))
            row = cur.fetchone()

            if row:
                messagebox.showerror("Error", "Roll No already exists", parent=self.root)
            else:
                cur.execute(
                    "INSERT INTO student "
                    "(rollno, Name, email, gender, dob, contact, admission, course, state, city, pin, address) "
                    "VALUES (?,?,?,?,?,?,?,?,?,?,?,?)",
                    (
                        self.var_rollno.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get('1.0', END).strip()
                    )
                )

                con.commit()
                messagebox.showinfo("Success", "Student added successfully", parent=self.root)
                self.show()

            con.close()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def update(self):
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()

            if self.var_rollno.get() == "":
                messagebox.showerror("Error", "Roll No. is required", parent=self.root)
                return

            cur.execute("SELECT * FROM student WHERE rollno=?", (self.var_rollno.get(),))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Roll No", parent=self.root)
            else:
                cur.execute(
                    """UPDATE student SET 
                    Name=?, email=?, gender=?, dob=?, contact=?, admission=?, course=?, state=?, city=?, pin=?, address=?
                    WHERE rollno=?""",
                    (
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_a_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0", END).strip(),
                        self.var_rollno.get()
                    )
                )

                con.commit()
                messagebox.showinfo("Success", "Student updated successfully", parent=self.root)
                self.show()

            con.close()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def delete(self):
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()

            if self.var_rollno.get() == "":
                messagebox.showerror("Error", "Roll No is required", parent=self.root)
                return

            cur.execute("SELECT * FROM student WHERE rollno=?", (self.var_rollno.get(),))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Invalid Roll No", parent=self.root)
            else:
                op = messagebox.askyesno(
                    "Confirm",
                    "Do you really want to delete?",
                    parent=self.root
                )

                if op:
                    cur.execute("DELETE FROM student WHERE rollno=?", (self.var_rollno.get(),))
                    con.commit()
                    messagebox.showinfo("Delete", "Student deleted", parent=self.root)
                    self.clear()

            con.close()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def clear(self):
        self.var_rollno.set("")
        self.var_name.set("")
        self.var_email.set("")
        self.var_gender.set("Select")
        self.var_dob.set("")
        self.var_contact.set("")
        self.var_a_date.set("")
        self.var_course.set("select")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pin.set("")
        self.txt_address.delete('1.0', END)
        self.var_search.set("")
        self.txt_rollno.config(state=NORMAL)
        self.show()

    def get_data(self, ev):
        f = self.CourseTable.focus()
        content = self.CourseTable.item(f)
        row = content['values']

        if row:
            self.var_rollno.set(row[0])
            self.var_name.set(row[1])
            self.var_email.set(row[2])
            self.var_gender.set(row[3])
            self.var_dob.set(row[4])
            self.var_contact.set(row[5])
            self.var_a_date.set(row[6])
            self.var_course.set(row[7])
            self.var_state.set(row[8])
            self.var_city.set(row[9])
            self.var_pin.set(row[10])

            self.txt_address.delete("1.0", END)
            self.txt_address.insert(END, row[11])

            self.txt_rollno.config(state='readonly')

    def show(self):
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()

            self.CourseTable.delete(*self.CourseTable.get_children())

            for row in rows:
                self.CourseTable.insert('', END, values=row)

            con.close()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def search(self):
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM student WHERE rollno=?", (self.var_search.get(),))
            row = cur.fetchone()

            if row:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('', END, values=row)
            else:
                messagebox.showerror("Error", "No record found", parent=self.root)

            con.close()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    def fetch_course(self):
        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()

            cur.execute("SELECT name FROM course")
            rows = cur.fetchall()

            self.course_list.clear()

            for row in rows:
                self.course_list.append(row[0])

            self.txt_course['values'] = self.course_list

            con.close()

        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = studentClass(root)
    root.mainloop()