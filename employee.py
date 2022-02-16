from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class employeeClass:
     def __init__(self,root):
         self.root=root
         self.root.geometry("1100x500+220+130")
         self.root.title("Inventory management system")
         self.root.config(bg="white")
         self.root.focus_force()
         # variable#
         self.var_searchby=StringVar()
         self.var_searchtxt=StringVar()
         
         self.var_emp_id=StringVar()  
         self.var_Gender=StringVar()
         self.var_contact=StringVar()
         self.var_email=StringVar()
         self.var_name=StringVar()
         self.var_dob=StringVar()
         self.var_doj=StringVar()
         self.var_pass=StringVar()
         self.var_salary=StringVar()
         self.var_utype=StringVar()
         #Search
         SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
         SearchFrame.place(x=250,y=20,width=600,height=70)
          
          #option 
         cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
         cmb_search.place(x=10,y=10,width=180)  
         cmb_search.current(0)

         txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
         btn_search=Button(SearchFrame,command=self.search,text="Search",font=("goudy old style",15),bg="lightgreen",fg="black",cursor="hand2").place(x=410,y=9,width=150,height=30)


         # for giving employee Title
         title=Label(self.root,text="EMPLOYEE DETAILS",font=("goudy old style",15),bg="blue",fg="white").place(x=50,y=100,width=1000)

         #content##########
         #for row 1
         lbl_empid=Label(self.root,text="Emp_Id",font=("goudy old style",15),bg="white").place(x=50,y=150)
         lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
         lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)
         

         txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
         cmb_gender=ttk.Combobox(self.root,textvariable=self.var_Gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
         cmb_gender.place(x=500,y=150,width=180)
         cmb_gender.current(0)
         txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=850,y=150,width=180)
         
         # for row 2

         lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
         lbl_dob=Label(self.root,text="D.O.B",font=("goudy old style",15),bg="white").place(x=350,y=190)
         lbl_doj=Label(self.root,text="D.O.J",font=("goudy old style",15),bg="white").place(x=750,y=190)
         

         txt_Name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
         txt_dob=Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15),bg="lightyellow").place(x=500,y=190,width=180)
         txt_doj=Entry(self.root,textvariable=self.var_doj,font=("goudy old style",15),bg="lightyellow").place(x=850,y=190,width=180)

         #for row 3
         lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="white").place(x=50,y=230)
         lbl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="white").place(x=350,y=230)
         lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="white").place(x=750,y=230)
         

         txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
         txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow").place(x=500,y=230,width=180)
         cmb_gender=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","Employee"),state='readonly',justify=CENTER,font=("goudy old style",15))
         cmb_gender.place(x=850,y=230,width=180)
         cmb_gender.current(0)
         
          # for row 4
         lbl_Address=Label(self.root,text="Address",font=("goudy old style",15),bg="white").place(x=50,y=270)
         lbl_salary=Label(self.root,text="Salary",font=("goudy old style",15),bg="white").place(x=500,y=270)
         
         self.txt_address=Text(self.root,font=("goudy old style",15),bg="lightyellow")
         self.txt_address.place(x=150,y=270,width=300,height=60)
         txt_salary=Entry(self.root,textvariable=self.var_salary,font=("goudy old style",15),bg="lightyellow").place(x=600,y=270,width=180)
         
         #for 4 btns
         btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="blue",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=27)
         btn_update=Button(self.root,text="Update",command=self.Update,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=27)
         btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=27)
         btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="grey",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=27)

#treeview
         emp_frame=Frame(self.root,bd=2,relief=RIDGE)
         emp_frame.place(x=0,y=350,relwidth=1,height=150)

         scrolly=Scrollbar(emp_frame,orient=VERTICAL) 
         scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)    
         self.EmployeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","dob","doj","pass","utype","address","salary"),yscrollcommand=scrolly,xscrollcommand=scrollx)
         scrollx.pack(side=BOTTOM,fill=X)
         scrolly.pack(side=RIGHT,fill=Y)
         scrollx.config(command=self.EmployeeTable.xview)
         scrollx.config(command=self.EmployeeTable.yview)
         

         self.EmployeeTable.heading("eid",text="EMP ID")
         self.EmployeeTable.heading("name",text="NAME")
         self.EmployeeTable.heading("email",text="E -mail")
         self.EmployeeTable.heading("gender",text="Gender")
         self.EmployeeTable.heading("contact",text="Contact")
         self.EmployeeTable.heading("dob",text="DOB")
         self.EmployeeTable.heading("doj",text="DOJ")
         self.EmployeeTable.heading("pass",text="Pass")
         self.EmployeeTable.heading("utype",text="User Type")
         self.EmployeeTable.heading("address",text="Address")
         self.EmployeeTable.heading("salary",text="Salary")
         self.EmployeeTable["show"]="headings"

         self.EmployeeTable.pack(fill=BOTH,expand=1)
        

         self.EmployeeTable["show"]="headings"

         self.EmployeeTable.column("eid",width=90)
         self.EmployeeTable.column("name",width=100)
         self.EmployeeTable.column("email",width=100)
         self.EmployeeTable.column("gender",width=100)
         self.EmployeeTable.column("contact",width=100)
         self.EmployeeTable.column("dob",width=100)
         self.EmployeeTable.column("doj",width=100)
         self.EmployeeTable.column("pass",width=100)
         self.EmployeeTable.column("utype",width=100)
         self.EmployeeTable.column("address",width=100)
         self.EmployeeTable.column("salary",width=100)
         self.EmployeeTable.bind("<ButtonRelease-1>",self.get_data)
         self.show()
#functions###########################################################################################################
     def add(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         try:
             if self.var_emp_id.get()=="":
                 messagebox.showerror("Error",f"Employee ID required",parent=self.root)
             else:
                 cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                 row=cur.fetchone()
                 if row!=None:
                     messagebox.showerror("Error",f"Employee ID already assigned,try with different ID",parent=self.root)
                 else:
                     cur.execute("Insert into employee(eid,name,email,gender,contact,dob,doj,pass,utype,address,salary)values(?,?,?,?,?,?,?,?,?,?,?)",(
                                          self.var_emp_id.get(),  
                                          self.var_name.get(),
                                          self.var_email.get(),
                                          self.var_Gender.get(),
                                          self.var_contact.get(),
                                          
                                          self.var_dob.get(),
                                          self.var_doj.get(),

                                          self.var_pass.get(),
                                          self.var_utype.get(),
                                          self.txt_address.get('1.0',END),
                                          self.var_salary.get(),
                                            
                     ))    
                     con.commit()
                     messagebox.showinfo("save","Employee added sucessfully",parent=self.root)
                     self.show()
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

     def show(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         try:
             cur.execute("select * from employee")
             rows=cur.fetchall()
             self.EmployeeTable.delete(*self.EmployeeTable.get_children())
             for row in rows:
                 self.EmployeeTable.insert('',END,values=row)

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

     def get_data(self,ev):    
         f=self.EmployeeTable.focus()
         content=(self.EmployeeTable.item(f))
         row=content['values']
         print(row)
         self.var_emp_id.set(row[0]),  
         self.var_name.set(row[1])
         self.var_email.set(row[2])
         self.var_Gender.set(row[3])
         self.var_contact.set(row[4])
                                          
         self.var_dob.set(row[5])
         self.var_doj.set(row[6])

         self.var_pass.set(row[7])
         self.var_utype.set(row[8])
         self.txt_address.delete('1.0',END)
         self.txt_address.insert(END,row[9])
         
         self.var_salary.set(row[10])
#update button##################################################################################################################################3
     def Update(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         try:
             if self.var_emp_id.get()=="":
                 messagebox.showerror("Error",f"Employee ID required",parent=self.root)
             else:
                 cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error",f"Employee ID is invalid",parent=self.root)
                 else:
                     cur.execute("Update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?",(
                                          
                                          self.var_name.get(),
                                          self.var_email.get(),
                                          self.var_Gender.get(),
                                          self.var_contact.get(),
                                          
                                          self.var_dob.get(),
                                          self.var_doj.get(),

                                          self.var_pass.get(),
                                          self.var_utype.get(),
                                          self.txt_address.get('1.0',END),
                                          self.var_salary.get(),
                                          self.var_emp_id.get(),    
                     ))    
                     con.commit()
                     messagebox.showinfo("Updated","Employee updated sucessfully",parent=self.root)
                     self.show()
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
    ###########delete Btn
     def delete(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         if self.var_emp_id.get()=="":
                 messagebox.showerror("Error",f"Employee ID required",parent=self.root)
         else:
                 cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error",f"Employee ID is invalid",parent=self.root)
                 else:
                     op=messagebox.askyesno("Do you Really want to delete",parent=self.root)
                     if op==True:
                        cur.execute(" Delete from  employee  where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Employee Deleted sucessfully",parent=self.root)
                        self.show()
                        self.clear()
     ##################for clear btn
     def clear(self):
                      self.var_emp_id.set("") 
                      self.var_name.set("")
                      self.var_email.set("") 
                      self.var_Gender.set("Select")
                      self.var_contact.set("")
                                          
                      self.var_dob.set("")
                      self.var_doj.set(""),

                      self.var_pass.set(""),
                      self.var_utype.set("Admin"),
                      self.txt_address.delete('1.0',END)
                      self.var_salary.set(""),
                      self.show()
                                             
     #for search btn
     def search(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         try:
             if self.var_searchby.get()=="Select":
                 messagebox.showerror("Error","Select search by option",parent=self.root)
             elif self.var_searchtxt.get()=="":
                 messagebox.showerror("Error","Please select By which field you want to search",parent=self.root)
             else:    
                 cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                 rows=cur.fetchall()
                 if len(rows)!=0:
                     self.EmployeeTable.delete(*self.EmployeeTable.get_children())
                     for row in rows:
                         self.EmployeeTable.insert('',END,values=row)
                 else:
                    messagebox.showerror("Error","No record found",parent=self.root)
                
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
                  



if __name__  =="__main__":                    
    root=Tk()
    obj=employeeClass(root)
    root.mainloop()       