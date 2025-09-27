from tkinter import *
from PIL import Image, ImageTk

class FirstPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System - First Page")
        self.root.geometry("900x600")
        self.root.config(bg="#0b2f56")  # Background color similar to 2nd image (dark blue)

        # ===== Top Header =====
        header = Frame(self.root, bg="#0b2f56", height=60)
        header.pack(fill=X)

        contact_lbl = Label(header, text="📞 +1-507-460-3586   ✉ info@xyz.com", 
                            fg="white", bg="#0b2f56", font=("Arial", 12, "bold"))
        contact_lbl.pack(side=LEFT, padx=10)

        signup_btn = Button(header, text="Sign Up", bg="orange", fg="white", 
                            font=("Arial", 12, "bold"), relief=FLAT, cursor="hand2")
        signup_btn.pack(side=RIGHT, padx=15)

        login_btn = Button(header, text="Login", bg="white", fg="black", 
                           font=("Arial", 12, "bold"), relief=FLAT, cursor="hand2")
        login_btn.pack(side=RIGHT, padx=10)

        # ===== Logo Section =====
        logo_frame = Frame(self.root, bg="white", height=120)
        logo_frame.pack(fill=X)

        # Add a sample logo (replace with your own if needed)
        logo_lbl = Label(logo_frame, text="🎓 ERP BASED STUDENT MANAGEMENT SYSTEM", font=("Arial", 28, "bold"), bg="white", fg="#0b2f56")
        logo_lbl.pack(pady=20)

        # ===== Menu Section =====
        menu_frame = Frame(self.root, bg="#0b2f56", height=50)
        menu_frame.pack(fill=X)

        menu_btns = ["Home", "About", "Modules", "Pricing", "Contact Us"]
        for btn in menu_btns:
            b = Button(menu_frame, text=btn, font=("Arial", 12, "bold"), bg="#0b2f56", 
                       fg="white", activebackground="orange", activeforeground="white", relief=FLAT, cursor="hand2")
            b.pack(side=LEFT, padx=20, pady=10)

        # ===== Center Section =====
        center_frame = Frame(self.root, bg="#e6f0fa")
        center_frame.pack(fill=BOTH, expand=True)

        welcome_lbl = Label(center_frame, text="Welcome to ERP-Based Student Management System", 
                            font=("Arial", 18, "bold"), bg="#e6f0fa", fg="#0b2f56")
        welcome_lbl.pack(pady=30)

        desc_lbl = Label(center_frame, text="Manage Admissions, Academics, Fees, Results, Library, Hostel and More", 
                         font=("Arial", 14), bg="#e6f0fa", fg="black")
        desc_lbl.pack(pady=10)

        # ===== Action Buttons =====
        btn_frame = Frame(center_frame, bg="#e6f0fa")
        btn_frame.pack(pady=30)

        student_btn = Button(btn_frame, text="Student Management", width=20, height=2, bg="#0b2f56", fg="white", font=("Arial", 12, "bold"))
        student_btn.grid(row=0, column=0, padx=20, pady=10)

        result_btn = Button(btn_frame, text="Result Management", width=20, height=2, bg="#0b2f56", fg="white", font=("Arial", 12, "bold"))
        result_btn.grid(row=0, column=1, padx=20, pady=10)

        fees_btn = Button(btn_frame, text="Fee & Finance", width=20, height=2, bg="#0b2f56", fg="white", font=("Arial", 12, "bold"))
        fees_btn.grid(row=1, column=0, padx=20, pady=10)

        library_btn = Button(btn_frame, text="Library Management", width=20, height=2, bg="#0b2f56", fg="white", font=("Arial", 12, "bold"))
        library_btn.grid(row=1, column=1, padx=20, pady=10)

        # ===== Footer =====
        footer = Label(self.root, text="© 2025 GeniusEDU Management System Pvt Ltd", 
                       font=("Arial", 10, "bold"), bg="#0b2f56", fg="white")
        footer.pack(side=BOTTOM, fill=X)

# Run the app
if __name__ == "__main__":
    root = Tk()
    obj = FirstPage(root)
    root.mainloop()
