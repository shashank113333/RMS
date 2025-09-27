from tkinter import *
from tkinter import messagebox, ttk
import mysql.connector
from register import Register
import os

class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Window")
        self.root.geometry("500x450+500+200")
        self.root.config(bg="white")

        # Variables
        self.var_email = StringVar()
        self.var_password = StringVar()
        self.var_remember = IntVar()

        frame = Frame(self.root, bg="white")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=350)

        title = Label(frame, text="LOGIN HERE", font=("times new roman", 30, "bold"), bg="white", fg="green")
        title.place(relx=0.5, y=20, anchor="center")

        # Email
        Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=70)
        self.txt_email = Entry(frame, textvariable=self.var_email, font=("times new roman", 15), bg="lightgray")
        self.txt_email.place(x=50, y=100, width=300)

        # Password
        Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=140)
        self.txt_password = Entry(frame, textvariable=self.var_password, show="*", font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=50, y=170, width=300)

        # Remember Me & Forgot Password
        self.chk_remember = Checkbutton(frame, text="Remember Me", variable=self.var_remember, onvalue=1, offvalue=0, bg="white", font=("times new roman", 12))
        self.chk_remember.place(x=50, y=205)

        btn_forgot = Button(frame, text="Forgot Password?", font=("times new roman", 12, "underline"), bg="white", fg="blue", bd=0, cursor="hand2", command=self.forgot_password_window)
        btn_forgot.place(x=220, y=205)

        # Login Button
        Button(frame, text="Login", font=("times new roman", 15, "bold"), bg="green", fg="white", command=self.login_user).place(relx=0.5, y=280, anchor="center", width=100)

        # Register Option
        lbl_reg = Label(frame, text="Don't have an account?", font=("times new roman", 12), bg="white")
        lbl_reg.place(x=90, y=320)

        btn_register = Button(frame, text="Register", font=("times new roman", 12, "bold"), bg="white", fg="blue", bd=0, cursor="hand2", command=self.open_register_window)
        btn_register.place(x=240, y=320)

    def login_user(self):
        if self.var_email.get() == "" or self.var_password.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                con = mysql.connector.connect(
                    host="localhost",
                    port=3307,
                    user="root",
                    password="1234",
                    database="employee2"
                )
                cur = con.cursor()
                cur.execute("SELECT * FROM employee WHERE email=%s AND password=%s",
                            (self.var_email.get(), self.var_password.get()))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Invalid Email or Password", parent=self.root)
                else:
                    messagebox.showinfo("Success", f"Welcome {self.txt_email.get()}", parent=self.root)
                    self.root.destroy()
                    os.system("python dashboard.py")
                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)

    def open_register_window(self):
        self.root.destroy()
        root2 = Tk()
        Register(root2)
        root2.mainloop()

    def forgot_password_window(self):
        self.root2 = Toplevel()
        self.root2.title("Reset Password")
        self.root2.geometry("400x400+500+200")
        self.root2.config(bg="white")

        Label(self.root2, text="Reset Password", font=("times new roman", 20, "bold"), fg="red", bg="white").place(x=90, y=30)

        # Email
        Label(self.root2, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=80)
        self.txt_email_forgot = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
        self.txt_email_forgot.place(x=50, y=110, width=300)

        # Security Question
        Label(self.root2, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=150)
        self.cmb_quest = ttk.Combobox(self.root2, font=("times new roman", 13), state='readonly', justify=CENTER)
        self.cmb_quest['values'] = ("Select", "Your Birth Place", "Your Pet Name", "Your Best Friend Name")
        self.cmb_quest.place(x=50, y=180, width=300)
        self.cmb_quest.current(0)

        # Answer
        Label(self.root2, text="Answer", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=220)
        self.txt_answer = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
        self.txt_answer.place(x=50, y=250, width=300)

        # New Password
        Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white", fg="gray").place(x=50, y=290)
        self.txt_new_pass = Entry(self.root2, font=("times new roman", 15), bg="lightgray")
        self.txt_new_pass.place(x=50, y=320, width=300)

        # Reset Button
        Button(self.root2, text="Reset Password", font=("times new roman", 15, "bold"), bg="green", fg="white", command=self.reset_password).place(relx=0.5, y=370, anchor="center")

    def reset_password(self):
        if (self.txt_email_forgot.get() == "" or
            self.cmb_quest.get() == "Select" or
            self.txt_answer.get() == "" or
            self.txt_new_pass.get() == ""):
            messagebox.showerror("Error", "All fields are required", parent=self.root2)
        else:
            try:
                # Connect to MySQL (XAMPP)
                con = mysql.connector.connect(
                    host="localhost",
                    port=3307,
                    user="root",
                    password="1234",
                    database="employee2"
                )
                cur = con.cursor()

                # DEBUG: Print input values to terminal
                print("Debug Info -->", self.txt_email_forgot.get(), self.cmb_quest.get(), self.txt_answer.get())

                # Check if security question + answer are correct
                cur.execute("SELECT * FROM employee WHERE email=%s AND questions=%s AND answer=%s",
                            (self.txt_email_forgot.get(), self.cmb_quest.get(), self.txt_answer.get()))
                row = cur.fetchone()

                if row is None:
                    messagebox.showerror("Error", "Incorrect security question or answer", parent=self.root2)
                else:
                    # Update password
                    cur.execute("UPDATE employee SET password=%s WHERE email=%s",
                                (self.txt_new_pass.get(), self.txt_email_forgot.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Password reset successfully", parent=self.root2)
                    self.root2.destroy()

                con.close()
            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root2)

# Run the App
if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()
