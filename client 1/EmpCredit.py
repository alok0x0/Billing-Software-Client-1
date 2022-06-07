from tkinter import *
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
import sqlite3
class employeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Hotel Management")
        self.root.config(bg="white")
        self.root.focus_force()




        #====searchFrame===
        SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
        SearchFrame.place(x=250,y=20,width=600,height=70)


        #===options===
        cmb_search=ttk.Combobox(SearchFrame,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=10,width=180)
        cmb_search.current(0)

        txt_search=Entry(SearchFrame,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search=Button(SearchFrame,text="search",font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        # ===title===
        title = Label(self.root, text="Credit Details", font=("goudy old style", 15), bg="#0f4d7d", fg="white").place(
            x=50, y=100, width=1000)

        #===Content===
        #==row1==
        lbl_customerid=Label(self.root,text="Cust ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
        lbl_date=Label(self.root,text="Date",font=("goudy old style",15),bg="white").place(x=350,y=150)
        lbl_duedate=Label(self.root,text="Due Date",font=("goudy old style",15),bg="white").place(x=750,y=150)

        txt_customerid = Entry(self.root, font=("goudy old style", 15),
                          bg="lightyellow").place(x=150, y=150, width=180)
        # txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white").place(x=500,y=150,width=180)
        # cmb_gender = ttk.Combobox(self.root, values=("Select", "Male", "Female", "Other"),
        #                           state='readonly', justify=CENTER, font=("goudy old style", 15))
        # cmb_gender.place(x=500, y=150, width=180)
        # cmb_gender.current(0)
        txt_date = Entry(self.root, font=("goudy old style", 15),
                            bg="lightyellow").place(x=500, y=150, width=180)
        txt_duedate = Entry(self.root, font=("goudy old style", 15),
                            bg="lightyellow").place(x=850, y=150, width=180)

        # ==row2==
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 15), bg="white").place(x=50, y=190)
        lbl_paymentamt = Label(self.root, text="Payment Amt", font=("goudy old style", 15), bg="white").place(x=350, y=190)
        lbl_dueamt = Label(self.root, text="Due Amt", font=("goudy old style", 15), bg="white").place(x=750, y=190)

        txt_name = Entry(self.root,  font=("goudy old style", 15), bg="lightyellow").place(
            x=150, y=190, width=180)
        txt_paymentamt = Entry(self.root, font=("goudy old style", 15), bg="lightyellow").place(
            x=500, y=190, width=180)
        txt_dueamt = Entry(self.root, font=("goudy old style", 15), bg="lightyellow").place(
            x=850, y=190, width=180)

        # ==row3==
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 15), bg="white").place(x=50, y=230)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 15), bg="white").place(x=350, y=230)
        lbl_status = Label(self.root, text="Status", font=("goudy old style", 15), bg="white").place(x=750, y=230)

        txt_email = Entry(self.root,  font=("goudy old style", 15), bg="lightyellow").place(
            x=150, y=230, width=180)
        txt_contact = Entry(self.root, font=("goudy old style", 15), bg="lightyellow").place(
            x=500, y=230, width=180)
        # txt_utype=Entry(self.root,textvariable=self.var_utype,font=("goudy old style",15),bg="lightyellow").place(x=850,y=230,width=180)
        cmb_status = ttk.Combobox(self.root, values=("Paid", "Unpaid"), state='readonly',
                                 justify=CENTER, font=("goudy old style", 15))
        cmb_status.place(x=850, y=230, width=180)
        cmb_status.current(0)

        # ==row4==
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 15), bg="white").place(x=50, y=270)
        # lbl_salary = Label(self.root, text="Salary", font=("goudy old style", 15), bg="white").place(x=500, y=270)

        self.txt_address = Text(self.root, font=("goudy old style", 15), bg="lightyellow")
        self.txt_address.place(x=150, y=270, width=300, height=60)
        # txt_salary = Entry(self.root,  font=("goudy old style", 15),
        #                    bg="lightyellow").place(x=600, y=270, width=180)

        # # ===buttons===
        btn_add = Button(self.root, text="Save", font=("goudy old style", 15), bg="#2196f3",
                         fg="white", cursor="hand2").place(x=500, y=305, width=110, height=28)
        btn_update = Button(self.root, text="Update",  font=("goudy old style", 15), bg="#4caf50",
                            fg="white", cursor="hand2").place(x=660, y=305, width=110, height=28)
        btn_delete = Button(self.root, text="Delete",  font=("goudy old style", 15), bg="#f44336",
                            fg="white", cursor="hand2").place(x=810, y=305, width=110, height=28)
        btn_clear = Button(self.root, text="Clear",  font=("goudy old style", 15), bg="#607d8b",
                           fg="white", cursor="hand2").place(x=960, y=305, width=110, height=28)

        #===Employee Details===
        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=150)


        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx= Scrollbar(emp_frame, orient=HORIZONTAL)

        self.EmployeeTable = ttk.Treeview(emp_frame, columns=(
        "cid", "name", "email", "date", "duedate", "paymentamt", "dueamt", "contact", "status", "address"),
                                          yscrollcommand=scrolly.set, xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.EmployeeTable.xview)
        scrolly.config(command=self.EmployeeTable.yview)

        self.EmployeeTable.heading("cid", text="CUST ID")
        self.EmployeeTable.heading("name", text="Name")
        self.EmployeeTable.heading("email", text="Email")
        self.EmployeeTable.heading("date", text="Date")
        self.EmployeeTable.heading("duedate", text="Due Date")
        self.EmployeeTable.heading("paymentamt", text="Payment Amt")
        self.EmployeeTable.heading("dueamt", text="Due Amt")
        self.EmployeeTable.heading("contact", text="Contact")
        self.EmployeeTable.heading("status", text="Status")
        self.EmployeeTable.heading("address", text="Address")

        self.EmployeeTable["show"]="headings"

        self.EmployeeTable.column("cid", width=90)
        self.EmployeeTable.column("name", width=100)
        self.EmployeeTable.column("email", width=100)
        self.EmployeeTable.column("date", width=100)
        self.EmployeeTable.column("duedate", width=100)
        self.EmployeeTable.column("paymentamt", width=100)
        self.EmployeeTable.column("dueamt", width=100)
        self.EmployeeTable.column("contact", width=100)
        self.EmployeeTable.column("status", width=100)
        self.EmployeeTable.column("address", width=100)
        self.EmployeeTable.pack(fill=BOTH, expand=1)
        # self.EmployeeTable.bind("<ButtonRelease-1>", self.get_data)




if __name__=="__main__":
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()