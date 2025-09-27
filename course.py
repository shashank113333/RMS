from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("School Result Management System")
        self.root.geometry("1200x600+80+100")
        self.root.config(bg="white")
        self.root.focus_force()

        #==== Title Label ====
        title = Label(self.root, text="Manage Courses Detail",
                      font=("goudy old style", 20, "bold"),
                      bg="#033054", fg="white")
        title.place(x=0, y=15, relwidth=1, height=55)

        #====== Variables ======
        self.var_course = StringVar()
        self.var_duration = StringVar()
        self.var_charges = StringVar()

        # ===== Labels =====
        Label(self.root, text="Course Name", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=90)
        Label(self.root, text="Duration", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=140)
        Label(self.root, text="Charges", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=190)
        Label(self.root, text="Description", font=("goudy old style", 15, 'bold'), bg='white').place(x=10, y=240)

        # ===== Entry Fields =====
        self.txt_courseName = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.txt_courseName.place(x=150, y=90, width=200)

        self.txt_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.txt_duration.place(x=150, y=140, width=200)

        self.txt_charges = Entry(self.root, textvariable=self.var_charges, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.txt_charges.place(x=150, y=190, width=200)

        self.txt_description = Text(self.root, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        self.txt_description.place(x=150, y=240, width=500, height=130)

        #==== Buttons ====
        self.btn_save = Button(self.root, text='Save', font=("goudy old style", 15, 'bold'), bg='#2196f3', fg="white", cursor="hand2", command=self.add)
        self.btn_save.place(x=150, y=400, width=110, height=40)

        self.btn_update = Button(self.root, text='Update',
                                 font=("goudy old style", 15, 'bold'),
                                 bg='#4caf50', fg="white",
                                 cursor="hand2", command=self.update)
        self.btn_update.place(x=270, y=400, width=110, height=40)

        self.btn_delete = Button(self.root, text='Delete', font=("goudy old style", 15, 'bold'), bg='#f44336', fg="white", cursor="hand2", command=self.delete)
        self.btn_delete.place(x=390, y=400, width=110, height=40)

        self.btn_clear = Button(self.root, text='Clear', font=("goudy old style", 15, 'bold'), bg='#607d8b', fg="white", cursor="hand2", command=self.clear)
        self.btn_clear.place(x=510, y=400, width=110, height=40)

        #==== Search Panel ====
        self.var_search=StringVar()
        lbl_search_courseName = Label(self.root, text=" Course Name:", font=("goudy old style", 15, 'bold'), bg='white')
        lbl_search_courseName.place(x=940, y=110)

        txt_courseName = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 15, 'bold'), bg='lightyellow')
        txt_courseName.place(x=1090, y=110, width=220)

        btn_search = Button(self.root, text='Search', font=("goudy old style", 15, 'bold'), bg='#03a9f4', fg="white", cursor="hand2", command=self.search).place(x=1330, y=100, width=180, height=40)

       #====== content ========
       
        self.C_Frame = Frame(self.root, bd= 2, relief= RIDGE)
        self.C_Frame.place(x=920,y=200,width=600,height=550)


        scrolly= Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx= Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable = ttk.Treeview(self.C_Frame, columns=("C_id","Name","Duration","Charges","Description"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        
        
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command= self.CourseTable.xview)
        scrolly.config(command= self.CourseTable.yview)



        self.CourseTable.heading("C_id",text="Course ID")
        self.CourseTable.heading("Name",text="Name")
        self.CourseTable.heading("Duration",text="Duration")
        self.CourseTable.heading("Charges",text="Charges")
        self.CourseTable.heading("Description",text="Description")
        self.CourseTable["show"]='headings'
        self.CourseTable.column("C_id",width=100)
        self.CourseTable.column("Name",width=150)
        self.CourseTable.column("Duration",width=150)
        self.CourseTable.column("Charges",width=100)
        self.CourseTable.column("Description",width=200)
        self.CourseTable.pack(fill=BOTH, expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()


        #======== ====================
        #===== clear button work========


        
    def clear(self):    
        self.show()
        self.var_course.set("")
        self.var_duration.set("")
        self.var_charges.set("")
        self.var_search.set("")
        self.txt_description.delete('1.0',END)
        self.txt_courseName.config(state=NORMAL)
        #==============  delete button work======

    def delete(self):    
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            course_name = self.var_course.get()
            if course_name == "":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
                return  # Stop here to avoid further execution

            cur.execute("SELECT * FROM course WHERE name=?", (course_name,))
            row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Please select a course from the list", parent=self.root)
            else:
                op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
            if op:
                cur.execute("DELETE FROM course WHERE name=?", (course_name,))
                con.commit()
                messagebox.showinfo("Deleted", "Course deleted successfully", parent=self.root)
                self.clear()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)


         
        

    
    
    def get_data(self,ev):
        self.txt_courseName.config(state='readonly')
        self.txt_courseName
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        #print(row)
        self.var_course.set(row[1])
        self.var_duration.set(row[2])
        self.var_charges.set(row[3])
        #self.var_course.set(row[4])
        self.txt_description.delete('1.0',END)
        self.txt_description.insert(END,row[4])



    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_course.get()=="":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_course.get(),))
                row = cur.fetchone()
            if row != None:
                    messagebox.showerror("Error", "Course already exists", parent=self.root)

            else:
                # Insert the new course
                cur.execute("INSERT INTO course (name,duration,charges,description) VALUES (?,?,?,?)",(
                    self.var_course.get(),
                    self.var_duration.get(),
                    self.var_charges.get(),
                    self.txt_description.get("1.0",END)
                ),
                )
                con.commit()
                messagebox.showinfo("Success", "Course added successfully", parent=self.root)
                self.show()  # Optional: Refresh the displayed list if you have one
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)


  #========  update button====

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()

        try:
            if self.var_course.get() == "":
                messagebox.showerror("Error", "Course Name is required", parent=self.root)
            else:
                cur.execute("select * from course where name=?", (self.var_course.get(),))
                row = cur.fetchone()

            if row is None:
                messagebox.showerror("Error", "Select course from the list to update", parent=self.root)
            else:
                cur.execute("UPDATE course SET duration=?, charges=?, description=? WHERE name=?", (
                    self.var_duration.get(),
                    self.var_charges.get(),
                    self.txt_description.get("1.0", END).strip(),
                    self.var_course.get()
                ))
                con.commit()
                messagebox.showinfo("Success", "Course updated successfully", parent=self.root)
                self.show()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

   




   ##==================================
    def show(self):
        try:
            con = sqlite3.connect(database="rms.db")
            cur = con.cursor()
            cur.execute("select * from course ")
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}",parent=self.root)
        finally:    
            con.close()

            
 #====== search button work=======
    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            search_term = self.var_search.get()
            cur.execute("SELECT * FROM course WHERE name LIKE ?", ('%' + search_term + '%',))
            rows = cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('', END, values=row)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)






# Only for testing
if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()
