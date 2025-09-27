from tkinter import *
from tkinter import messagebox


class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("ERP-Based Student Management System - Home Page")
        self.root.geometry("900x600")
        self.root.config(bg="#0b2f56")  # Dark Blue Background

        # ====== Header Section ======
        header = Frame(self.root, bg="#0b2f56", height=60)
        header.pack(fill=X)

        title = Label(header, text="ERP-Based Student Management System",
                      font=("Arial", 20, "bold"), bg="#0b2f56", fg="white")
        title.pack(pady=10)

        # ====== Welcome Text ======
        welcome_lbl = Label(self.root, text="Welcome to Genius EDU Management System",
                            font=("Arial", 18, "bold"), bg="#0b2f56", fg="white")
        welcome_lbl.pack(pady=30)

        sub_lbl = Label(self.root, text="Please select your login type",
                        font=("Arial", 14), bg="#0b2f56", fg="lightgray")
        sub_lbl.pack(pady=5)

        # ====== Login Buttons ======
        btn_frame = Frame(self.root, bg="#0b2f56")
        btn_frame.pack(pady=40)

        admin_btn = Button(btn_frame, text="Admin Login", width=20, height=2,
                           bg="orange", fg="white", font=("Arial", 14, "bold"),
                           cursor="hand2", command=self.admin_login)
        admin_btn.grid(row=0, column=0, padx=30, pady=20)

        teacher_btn = Button(btn_frame, text="Teacher Login", width=20, height=2,
                             bg="green", fg="white", font=("Arial", 14, "bold"),
                             cursor="hand2", command=self.teacher_login)
        teacher_btn.grid(row=0, column=1, padx=30, pady=20)

        student_btn = Button(btn_frame, text="Student Login", width=20, height=2,
                             bg="blue", fg="white", font=("Arial", 14, "bold"),
                             cursor="hand2", command=self.student_login)
        student_btn.grid(row=1, column=0, columnspan=2, pady=20)

        # ====== Footer ======
        footer = Label(self.root, text="© 2025 Genius EDU Management System Pvt Ltd | Contact: info@geniusedusoft.com",
                       font=("Arial", 10, "bold"), bg="#0b2f56", fg="white")
        footer.pack(side=BOTTOM, fill=X, pady=10)

    # ===== Functions to Open Login Windows =====
    def admin_login(self):
        self.open_login_window("Admin Login", "orange")

    def teacher_login(self):
        self.open_login_window("Teacher Login", "green")

    def student_login(self):
        self.open_login_window("Student Login", "blue")

    def open_login_window(self, title, color):
        login_win = Toplevel(self.root)
        login_win.title(title)
        login_win.geometry("400x300")
        login_win.config(bg="#0b2f56")

        lbl_title = Label(login_win, text=title, font=("Arial", 18, "bold"),
                          bg="#0b2f56", fg="white")
        lbl_title.pack(pady=20)

        lbl_user = Label(login_win, text="Username:", font=("Arial", 12, "bold"),
                         bg="#0b2f56", fg="white")
        lbl_user.pack(pady=5)
        ent_user = Entry(login_win, font=("Arial", 12), width=25)
        ent_user.pack(pady=5)

        lbl_pass = Label(login_win, text="Password:", font=("Arial", 12, "bold"),
                         bg="#0b2f56", fg="white")
        lbl_pass.pack(pady=5)
        ent_pass = Entry(login_win, font=("Arial", 12), show="*", width=25)
        ent_pass.pack(pady=5)

        def do_login():
            username = ent_user.get()
            password = ent_pass.get()
            if username == "" or password == "":
                messagebox.showerror("Error", "All fields are required!", parent=login_win)
            else:
                messagebox.showinfo("Success", f"{title} Successful!", parent=login_win)
                login_win.destroy()  # Close login window after success

        login_btn = Button(login_win, text="Login", width=15, height=1,
                           bg=color, fg="white", font=("Arial", 12, "bold"),
                           cursor="hand2", command=do_login)
        login_btn.pack(pady=20)


# Run App
if __name__ == "__main__":
    root = Tk()
    obj = HomePage(root)
    root.mainloop()
