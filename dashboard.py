from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import subprocess
import sys
import os
import sqlite3  # Required for update_details()

# Dummy class imports (replace with actual implementations)
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass


class RMS:
    def __init__(self):
        self.root = Tk()
        self.root.title("Student Result Management System")
        self.root.geometry("1490x900+0+0")
        self.root.config(bg="white")

        # === Title ===
        title = Label(
            self.root,
            text="Student Result Management System",
            font=("goudy old style", 20, "bold"),
            bg="#033054",
            fg="white",
            padx=10,
            compound=LEFT
        )
        title.place(x=0, y=10, relwidth=1, height=50)

        # === Menu Frame ===
        M_Frame = LabelFrame(
            self.root,
            text="Menus",
            font=("times new roman", 15),
            bg="white",
            bd=2,
            relief=RIDGE
        )
        M_Frame.place(x=10, y=70, width=1500, height=80)

        # === Buttons ===
        Button(M_Frame, text="Course", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2", command=self.add_course).place(x=25, y=10, width=200, height=40)
        Button(M_Frame, text="Student", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2", command=self.add_student).place(x=280, y=10, width=200, height=40)
        Button(M_Frame, text="Result", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2", command=self.add_result).place(x=530, y=10, width=200, height=40)
        Button(M_Frame, text="View  Student  Result", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2", command=self.add_report).place(x=780, y=10, width=220, height=40)
        Button(M_Frame, text="Logout", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2", command=self.logout).place(x=1050, y=10, width=200, height=40)
        Button(M_Frame, text="Exit", font=("goudy old style", 15, "bold"),
               bg="#0b5377", fg="white", cursor="hand2", command=self.exit_).place(x=1290, y=10, width=180, height=40)

        # === Content Window (Image Section) ===
        try:
            self.bg_image = Image.open("image/bg.jpg")
            self.bg_image = self.bg_image.resize((1080, 430), Image.Resampling.LANCZOS)
            self.bg_img = ImageTk.PhotoImage(self.bg_image)
            self.lbl_bg = Label(self.root, image=self.bg_img)
            self.lbl_bg.place(x=250, y=180, width=1080, height=430)
        except Exception as e:
            print("Error loading image:", e)

        # === Update Details ===
        self.lbl_student = Label(self.root, text="Total Students\n [ 0 ]", font=("goudy old style", 20), bd=10,
                                 relief=RIDGE, bg="blue", fg="white")
        self.lbl_student.place(x=150, y=620, width=300, height=100)

        self.lbl_course = Label(self.root, text="Total Courses\n [ 0 ]", font=("goudy old style", 20), bd=10,
                                relief=RIDGE, bg="green", fg="white")
        self.lbl_course.place(x=640, y=620, width=300, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n [ 0 ]", font=("goudy old style", 20), bd=10,
                                relief=RIDGE, bg="red", fg="white")
        self.lbl_result.place(x=1100, y=620, width=300, height=100)

        # === Footer ===
        footer = Label(
            self.root,
            text="SRMS - Student Result Management System\nContact Us for any Technical Issue: XY*******Z",
            font=("goudy old style", 15),
            bg="#262626",
            fg="white"
        )
        footer.pack(side=BOTTOM, fill=X)

        # === Call method to update data on dashboard ===
        self.update_details()

        self.root.mainloop()

    # === Update Dashboard Data ===
    def update_details(self):
        try:
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM course")
            cr = cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n [ {len(cr)} ]")
            self.lbl_course.after(200,self.update_details)

            cur.execute("SELECT * FROM student")
            st = cur.fetchall()
            self.lbl_student.config(text=f"Total Students\n [ {len(st)} ]")

            cur.execute("SELECT * FROM result")
            rs = cur.fetchall()
            self.lbl_result.config(text=f"Total Results\n [ {len(rs)} ]")

            con.close()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    # === Functions for Buttons ===
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op:
            self.root.destroy()
            os.system("python login.py")

    def exit_(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op:
            self.root.destroy()


# Run the app
if __name__ == "__main__":
    RMS()
