from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import os
import sys


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Registration Window")
        self.root.geometry("1100x700+0+0")
        self.root.config(bg="white")

        # ====== Variables ======
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_question = StringVar()
        self.var_answer = StringVar()
        self.var_password = StringVar()
        self.var_cpassword = StringVar()
        self.var_chk = IntVar()

        # ====== Register Frame ======
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=250, y=100, width=700, height=650)

        title = Label(
            frame1,
            text="REGISTER HERE",
            font=("times new roman", 20, "bold"),
            bg="white",
            fg="green"
        )
        title.place(x=50, y=30)

        # First Name
        Label(
            frame1,
            text="First Name",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray"
        ).place(x=50, y=100)

        self.txt_fname = Entry(
            frame1,
            textvariable=self.var_fname,
            font=("times new roman", 15),
            bg="lightgray"
        )
        self.txt_fname.place(x=50, y=130, width=250)

        # Last Name
        Label(
            frame1,
            text="Last Name",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray"
        ).place(x=370, y=100)

        self.txt_lname = Entry(
            frame1,
            textvariable=self.var_lname,
            font=("times new roman", 15),
            bg="lightgray"
        )
        self.txt_lname.place(x=370, y=130, width=250)

        # Contact
        Label(
            frame1,
            text="Contact No.",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray"
        ).place(x=50, y=170)

        # Contact me sirf numbers allow karne ke liye
        vcmd = (self.root.register(self.only_numbers), "%P")

        self.txt_contact = Entry(
            frame1,
            textvariable=self.var_contact,
            font=("times new roman", 15),
            bg="lightgray",
            validate="key",
            validatecommand=vcmd
        )
        self.txt_contact.place(x=50, y=200, width=250)

        # Email
        Label(
            frame1,
            text="Email",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray"
        ).place(x=370, y=170)

        self.txt_email = Entry(
            frame1,
            textvariable=self.var_email,
            font=("times new roman", 15),
            bg="lightgray"
        )
        self.txt_email.place(x=370, y=200, width=250)

        # Security Question
        Label(
            frame1,
            text="Security Question",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray"
        ).place(x=50, y=240)

        self.cmb_quest = ttk.Combobox(
            frame1,
            textvariable=self.var_question,
            font=("times new roman", 13),
            state="readonly"
        )
        self.cmb_quest["values"] = (
            "Select",
            "Your First Pet Name",
            "Your Birth Place",
            "Your Best Friend Name"
        )
        self.cmb_quest.current(0)
        self.cmb_quest.place(x=50, y=270, width=250)

        # Answer
        Label(
            frame1,
            text="Answer",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray"
        ).place(x=370, y=240)

        self.txt_answer = Entry(
            frame1,
            textvariable=self.var_answer,
            font=("times new roman", 15),
            bg="lightgray"
        )
        self.txt_answer.place(x=370, y=270, width=250)

        # Password
        Label(
            frame1,
            text="Password",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray"
        ).place(x=50, y=310)

        self.txt_password = Entry(
            frame1,
            textvariable=self.var_password,
            show="*",
            font=("times new roman", 15),
            bg="lightgray"
        )
        self.txt_password.place(x=50, y=340, width=250)

        # Confirm Password
        Label(
            frame1,
            text="Confirm Password",
            font=("times new roman", 15, "bold"),
            bg="white",
            fg="gray"
        ).place(x=370, y=310)

        self.txt_cpassword = Entry(
            frame1,
            textvariable=self.var_cpassword,
            show="*",
            font=("times new roman", 15),
            bg="lightgray"
        )
        self.txt_cpassword.place(x=370, y=340, width=250)

        # Terms & Conditions Checkbox
        Checkbutton(
            frame1,
            variable=self.var_chk,
            text="I Agree to the Terms & Conditions",
            onvalue=1,
            offvalue=0,
            font=("times new roman", 12),
            bg="white"
        ).place(x=50, y=385)

        # Register Button
        Button(
            frame1,
            text="Register",
            font=("times new roman", 15, "bold"),
            bg="green",
            fg="white",
            cursor="hand2",
            command=self.register_data
        ).place(x=250, y=435, width=200)

        # Login Option
        Label(
            frame1,
            text="Already have an account?",
            font=("times new roman", 12),
            bg="white",
            fg="gray"
        ).place(x=220, y=500)

        Button(
            frame1,
            text="Login",
            font=("times new roman", 12, "bold"),
            bg="white",
            fg="blue",
            bd=0,
            cursor="hand2",
            command=self.login_window
        ).place(x=390, y=498)

    # Sirf number allow karega aur max 10 digit
    def only_numbers(self, value):
        if value == "":
            return True

        if value.isdigit() and len(value) <= 10:
            return True

        return False

    def login_window(self):
        self.root.destroy()
        os.system(f'"{sys.executable}" login.py')

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_answer.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.cmb_quest.current(0)
        self.var_chk.set(0)

    def register_data(self):
        if (
            self.var_fname.get() == "" or
            self.var_lname.get() == "" or
            self.var_contact.get() == "" or
            self.var_email.get() == "" or
            self.var_question.get() == "Select" or
            self.var_answer.get() == "" or
            self.var_password.get() == "" or
            self.var_cpassword.get() == ""
        ):
            messagebox.showerror(
                "Error",
                "All fields are required",
                parent=self.root
            )

        elif len(self.var_contact.get()) != 10:
            messagebox.showerror(
                "Error",
                "Contact number must be 10 digits",
                parent=self.root
            )

        elif self.var_password.get() != self.var_cpassword.get():
            messagebox.showerror(
                "Error",
                "Password and Confirm Password should match",
                parent=self.root
            )

        elif self.var_chk.get() == 0:
            messagebox.showerror(
                "Error",
                "Please agree to the Terms & Conditions",
                parent=self.root
            )

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

                # Check if email already exists
                cur.execute(
                    "SELECT * FROM employee WHERE email=%s",
                    (self.var_email.get(),)
                )
                row = cur.fetchone()

                if row is not None:
                    messagebox.showerror(
                        "Error",
                        "User already exists with this email",
                        parent=self.root
                    )
                    con.close()

                else:
                    cur.execute(
                        "INSERT INTO employee "
                        "(f_name, l_name, contact, email, questions, answer, password) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (
                            self.var_fname.get(),
                            self.var_lname.get(),
                            self.var_contact.get(),
                            self.var_email.get(),
                            self.var_question.get(),
                            self.var_answer.get(),
                            self.var_password.get()
                        )
                    )

                    con.commit()
                    con.close()

                    messagebox.showinfo(
                        "Success",
                        f"Welcome {self.var_fname.get()}!\nRegistration Successful.",
                        parent=self.root
                    )

                    self.clear()
                    self.login_window()

            except Exception as es:
                messagebox.showerror(
                    "Error",
                    f"Error due to: {str(es)}",
                    parent=self.root
                )


# Run the App
if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()