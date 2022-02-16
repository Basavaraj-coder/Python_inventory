from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class SupplierClass:
     def __init__(self,root):
         self.root=root
         self.root.geometry("1100x500+220+130")
         self.root.title("Inventory management system")
         self.root.config(bg="white")
         self.root.focus_force()
         # variable#
         self.var_searchby=StringVar()
         self.var_searchtxt=StringVar()
          
         self.var_supplier_invoice=StringVar()  
         self.var_contact=StringVar()
         self.var_name=StringVar()
         #self.var_desc=StringVar()
        
         SearchFrame=LabelFrame(self.root,text="Search Supplier",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
         SearchFrame.place(x=250,y=20,width=600,height=70)
          
          #option 
         cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
         cmb_search.place(x=10,y=10,width=180)  
         cmb_search.current(0)

         txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
         btn_search=Button(SearchFrame,command=self.search,text="Search",font=("goudy old style",15),bg="lightgreen",fg="black",cursor="hand2").place(x=410,y=9,width=150,height=30)


         # for giving employee Title
         title=Label(self.root,text="SUPPLIER DETAILS",font=("goudy old style",15),bg="blue",fg="white").place(x=50,y=100,width=1000)

         #content##########
         #for row 1
         lbl_supplier_invoice=Label(self.root,text="Invoice No",font=("goudy old style",15),bg="white").place(x=50,y=150)
         txt_supplier_invoice=Entry(self.root,textvariable=self.var_supplier_invoice,font=("goudy old style",15),bg="lightyellow").place(x=150,y=150,width=180)
         
         # for row 2

         lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white").place(x=50,y=190)
         txt_Name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=150,y=190,width=180)
         
         #for row 3
         lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=50,y=230)
         txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=150,y=230,width=180)
         
          # for row 4
         lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white").place(x=50,y=270)
         
         self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
         self.txt_desc.place(x=150,y=270,width=300,height=60)
         
         #for 4 btns
         btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="blue",fg="white",cursor="hand2").place(x=500,y=305,width=110,height=27)
         btn_update=Button(self.root,text="Update",command=self.Update,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=620,y=305,width=110,height=27)
         btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=740,y=305,width=110,height=27)
         btn_clear=Button(self.root,text="Clear",command=self.clear,font=("goudy old style",15),bg="grey",fg="white",cursor="hand2").place(x=860,y=305,width=110,height=27)
           #=========employee details===================================================================# 
         emp_frame=Frame(self.root,bd=2,relief=RIDGE)
         emp_frame.place(x=0,y=350,relwidth=1,height=150)

         scrolly=Scrollbar(emp_frame,orient=VERTICAL) 
         scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)    
         self.SupplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly,xscrollcommand=scrollx)
         scrollx.pack(side=BOTTOM,fill=X)
         scrolly.pack(side=RIGHT,fill=Y)
         scrollx.config(command=self.SupplierTable.xview)
         scrollx.config(command=self.SupplierTable.yview)
         

         self.SupplierTable.heading("invoice",text="Invoice")
         self.SupplierTable.heading("name",text="NAME")
         self.SupplierTable.heading("contact",text="Contact")
         self.SupplierTable.heading("desc",text="Description")
         self.SupplierTable["show"]="headings"

         self.SupplierTable.pack(fill=BOTH,expand=1)
        

         self.SupplierTable["show"]="headings"

         self.SupplierTable.column("invoice",width=90)
         self.SupplierTable.column("name",width=100)
         self.SupplierTable.column("contact",width=100)
         self.SupplierTable.column("desc",width=100)
         self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)
         self.show()
#functions###########################################################################################################
     def add(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         try:
             if self.var_supplier_invoice.get()=="":
                 messagebox.showerror("Error",f"Invoice must be  required",parent=self.root)
             else:
                 cur.execute("Select * from supplier where invoice=?",(self.var_supplier_invoice.get(),))
                 row=cur.fetchone()
                 if row!=None:
                     messagebox.showerror("Error",f"Invoice no  already assigned,try with different ID",parent=self.root)
                 else:
                     cur.execute("Insert into supplier(invoice,name,contact,desc)values(?,?,?,?)",(
                                          self.var_supplier_invoice.get(),  
                                          self.var_name.get(),
                                          self.var_contact.get(),
                                          
                                          self.txt_desc.get('1.0',END),
                                            
                     ))    
                     con.commit()
                     messagebox.showinfo("save","Supplier added sucessfully",parent=self.root)
                     self.show()
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

     def show(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         try:
             cur.execute("select * from supplier")
             rows=cur.fetchall()
             self.SupplierTable.delete(*self.SupplierTable.get_children())
             for row in rows:
                 self.SupplierTable.insert('',END,values=row)

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

     def get_data(self,ev):    
         f=self.SupplierTable.focus()
         content=(self.SupplierTable.item(f))
         row=content['values']
         print(row)
         self.var_supplier_invoice.set(row[0]),  
         self.var_name.set(row[1])
         self.var_contact.set(row[2])
         
         self.txt_desc.delete('1.0',END)
         self.txt_desc.insert(END,row[3])
         
        #update button##################################################################################################################################3
     def Update(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         try:
             if self.var_supplier_invoice.get()=="":
                 messagebox.showerror("Error",f"Invoice no required",parent=self.root)
             else:
                 cur.execute("Select * from supplier where invoice=?",(self.var_supplier_invoice.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error",f"Invoice is invalid",parent=self.root)
                 else:
                     cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                          
                                          self.var_name.get(),
                                          self.var_contact.get(),
                                          
                                          self.txt_desc.get('1.0',END),
                                          self.var_supplier_invoice.get(),    
                     ))    
                     con.commit()
                     messagebox.showinfo("Updated","Supplier updated sucessfully",parent=self.root)
                     self.show()
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
    ###########delete Btn
     def delete(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         try:
          if self.var_supplier_invoice.get()=="":
                 messagebox.showerror("Error",f"Invoice no required",parent=self.root)
          else:
                 cur.execute("Select * from supplier where invoice=?",(self.var_supplier_invoice.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error",f"supplier no is invalid",parent=self.root)
                 else:
                     op=messagebox.askyesno("Do you Really want to delete",parent=self.root)
                     if op==True:
                        cur.execute(" Delete from  supplier  where invoice=?",(self.var_supplier_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier Deleted sucessfully",parent=self.root)
                        self.show()
                        self.clear()
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)             
     ##################for clear btn
     def clear(self):
                      self.var_supplier_invoice.set("") 
                      self.var_name.set("")
                      self.var_contact.set("")
                                          
                      self.txt_desc.delete('1.0',END)
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
                 cur.execute("select * from supplier where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                 rows=cur.fetchall()
                 if len(rows)!=0:
                     self.SupplierTable.delete(*self.SupplierTable.get_children())
                     for row in rows:
                         self.SupplierTable.insert('',END,values=row)
                 else:
                    messagebox.showerror("Error","No record found",parent=self.root)
                
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
                  



if __name__  =="__main__":                    
    root=Tk()
    obj=SupplierClass(root)
    root.mainloop()       