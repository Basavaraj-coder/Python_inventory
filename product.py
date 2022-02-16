from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class ProductClass:
     def __init__(self,root):
         self.root=root
         self.root.geometry("1100x500+220+130")
         self.root.title("Inventory management system")
         self.root.config(bg="white")
         self.root.focus_force()

         #****************************
         self.var_searchby=StringVar()
         self.var_searchtxt=StringVar()

         self.var_cat=StringVar()
         self.var_pid=StringVar()
         self.cat_list=[]
         self.sup_list=[]
         self.fetch_cat_sup()
         self.var_sup=StringVar()
         self.var_name=StringVar()
         self.var_price=StringVar()
         self.var_qty=StringVar()
         self.var_status=StringVar()
         #_______________Frame_________
         product_frame=Frame(self.root,bd=3,relief=RIDGE, bg="white")
         product_frame.place(x=10,y=10,width=450,height=480)
         #_______________title_______________
         title=Label(product_frame,text="Product Details",font=('goudy old style',18),bg="#0f4d7d", fg="white").pack(side=TOP,fill=X)
         #__________LABELS_________________
         lbl_category=Label(product_frame,text="Category",font=("goudy old style",),bg="white").place(x=30,y=60)
         lbl_supplier=Label(product_frame,text="Supplier",font=("goudy old style",),bg="white").place(x=30,y=110)
         lbl_PN=Label(product_frame,text="Name",font=("goudy old style",),bg="white").place(x=30,y=160)
         lbl_Price=Label(product_frame,text="Price",font=("goudy old style",),bg="white").place(x=30,y=210)
         lbl_Quantity=Label(product_frame,text="Quantity",font=("goudy old style",),bg="white").place(x=30,y=260)
         lbl_Status=Label(product_frame,text="Status",font=("goudy old style",),bg="white").place(x=30,y=310)

        #Coulumns******************88
         cmb_cat=ttk.Combobox(product_frame,textvariable=self.var_cat, values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
         cmb_cat.place(x=150,y=60,width=200)  
         cmb_cat.current(0)

         cmb_sup=ttk.Combobox(product_frame,textvariable=self.var_sup, values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))
         cmb_sup.place(x=150,y=110,width=200)  
         cmb_sup.current(0)

         txt_name=Entry(product_frame,textvariable=self.var_name, font=('goudy old style', 15),bg='lightyellow').place(x=150,y=160,width=200)
         txt_price=Entry(product_frame,textvariable=self.var_price, font=('goudy old style', 15),bg='lightyellow').place(x=150,y=210,width=200)
         txt_qty=Entry(product_frame,textvariable=self.var_qty, font=('goudy old style', 15),bg='lightyellow').place(x=150,y=260,width=200)

         cmb_status=ttk.Combobox(product_frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
         cmb_status.place(x=150,y=310,width=200)  
         cmb_status.current(0)
        
         btn_add=Button(product_frame,text="Save",command=self.add,font=("goudy old style",15),bg="blue",fg="white", cursor="hand2").place(x=10,y=400,width=100,height=40)
         btn_update=Button(product_frame,text="Update",command=self.Update,font=("goudy old style",15),bg="green",fg="white",cursor="hand2").place(x=120,y=400,width=100,height=40)
         btn_delete=Button(product_frame,text="Delete",command=self.delete,font=("goudy old style",15),bg="red",fg="white",cursor="hand2").place(x=230,y=400,width=100,height=40)
         btn_clear=Button(product_frame,text="Clear",command=self.clear,font=("goudy old style",15),bg="grey",fg="white",cursor="hand2").place(x=340,y=400,width=100,height=40)

          #Search
         SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,relief=RIDGE,bg="white")
         SearchFrame.place(x=480,y=10,width=600,height=80)
          
          #option 
         cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
         cmb_search.place(x=10,y=10,width=180)  
         cmb_search.current(0)

         txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
         btn_search=Button(SearchFrame,command=self.search,text="Search",font=("goudy old style",15),bg="lightgreen",fg="black",cursor="hand2").place(x=410,y=9,width=150,height=30)


        #treeview
         pframe=Frame(self.root,bd=2,relief=RIDGE)
         pframe.place(x=480,y=100,width=600,height=390)

         scrolly=Scrollbar(pframe,orient=VERTICAL) 
         scrollx=Scrollbar(pframe,orient=HORIZONTAL)   

         self.product_table=ttk.Treeview(pframe,columns=("pid","Supplier","Category","name","price","qty","status"),yscrollcommand=scrolly,xscrollcommand=scrollx)
         scrollx.pack(side=BOTTOM,fill=X)
         scrolly.pack(side=RIGHT,fill=Y)
         scrollx.config(command=self.product_table.xview)
         scrollx.config(command=self.product_table.yview)
         
         self.product_table.heading("pid",text="Product ID")
         self.product_table.heading("Category",text="Category")
         self.product_table.heading("Supplier",text="Supplier")
         self.product_table.heading("name",text="Name")
         self.product_table.heading("price",text="Price")
         self.product_table.heading("qty",text="Qty")
         self.product_table.heading("status",text="Status")
         
         self.product_table["show"]="headings"

         self.product_table.pack(fill=BOTH,expand=1)
        

         self.product_table["show"]="headings"

         self.product_table.column("pid",width=90)
         self.product_table.column("Category",width=100)
         self.product_table.column("Supplier",width=100)
         self.product_table.column("name",width=100)
         self.product_table.column("price",width=100)
         self.product_table.column("qty",width=100)
         self.product_table.column("status",width=100)
         self.product_table.pack(fill=BOTH, expand=1)
         self.product_table.bind("<ButtonRelease-1>",self.get_data)
         self.show()
        
#functions######################################################################################################### def fetch_cat_sup(self):

     def fetch_cat_sup(self):
         self.cat_list.append("Empty")
         self.sup_list.append("Empty")
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         try:
             cur.execute("Select name from category")
             cat=cur.fetchall()
            #  self.cat_list.append("Empty")
             if len(cat)>0:
                 del self.cat_list[:]
                 self.cat_list.append("select")
                 for i in cat:
                    self.cat_list.append(i[0])

             cur.execute("Select name from supplier")
             sup=cur.fetchall()
             if len(sup)>0:
                 del self.sup_list[:]
                 self.sup_list.append("select")
                 for i in sup:
                    self.sup_list.append(i[0])
            #  print(sup)

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
     def add(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         try:
             if self.var_cat.get()=="Select" or self.var_sup.get()=="Select" or self.var_name.get()=="":
                 messagebox.showerror("Error",f"All fields are required",parent=self.root)
             else:
                 cur.execute("Select * from product where name=?",(self.var_name.get(),))
                 row=cur.fetchone()
                 if row!=None:
                     messagebox.showerror("Error",f"Product already preesent,try with different ",parent=self.root)
                 else:
                     cur.execute("Insert into product(Category,Supplier,name,price,qty,status)values(?,?,?,?,?,?)",(
                                          self.var_cat.get(),  
                                          self.var_sup.get(),
                                          self.var_name.get(),
                                          self.var_price.get(),
                                          self.var_qty.get(),
                                          self.var_status.get(),
                                          ))    
                     con.commit()
                     messagebox.showinfo("save","Product added sucessfully",parent=self.root)
                     self.show()
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

     def show(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         try:
             cur.execute("select * from product")
             rows=cur.fetchall()
             self.product_table.delete(*self.product_table.get_children())
             for row in rows:
                 self.product_table.insert('',END,values=row)

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)

     def get_data(self,ev):    
         f=self.product_table.focus()
         content=(self.product_table.item(f))
         row=content['values']
        #  print(row)
         self.var_pid.set(row[0])
         self.var_sup.set(row[1])
         self.var_cat.set(row[2])
              
         self.var_name.set(row[3])
         self.var_price.set(row[4])
         self.var_qty.set(row[5])
         self.var_status.set(row[6])
#update button##################################################################################################################################3
     def Update(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         try:
             if self.var_pid.get()=="":
                 messagebox.showerror("Error",f"Select product from list",parent=self.root)
             else:
                 cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error",f"P ID is invalid",parent=self.root)
                 else:
                     cur.execute("Update product set Category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                                          self.var_cat.get(),  
                                          self.var_sup.get(),
                                          self.var_name.get(),
                                          self.var_price.get(),
                                          self.var_qty.get(),
                                          self.var_status.get(),
                                          self.var_pid.get()
                                          
                     ))    
                     con.commit()
                     messagebox.showinfo("Updated","Product updated sucessfully",parent=self.root)
                     self.show()
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
    ###########delete Btn
     def delete(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         if self.var_pid.get()=="":
                 messagebox.showerror("Error",f"Product ID required",parent=self.root)
         else:
                 cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error",f"Product ID is invalid",parent=self.root)
                 else:
                     op=messagebox.askyesno("Do you Really want to delete",parent=self.root)
                     if op==True:
                        cur.execute(" Delete from  product  where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","product Deleted sucessfully",parent=self.root)
                        self.show()
                        self.clear()
     ##################for clear btn
     def clear(self):
                      self.var_cat.set(""),  
                      self.var_sup.set(""),
                      self.var_name.set(""),
                      self.var_price.set(""),
                      self.var_qty.set(""),
                      self.var_status.set(""),
                      self.var_searchtxt.set("")
                      self.var_searchby.set("Select")
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
                 cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                 rows=cur.fetchall()
                 if len(rows)!=0:
                     self.product_table.delete(*self.product_table.get_children())
                     for row in rows:
                         self.product_table.insert('',END,values=row)
                 else:
                    messagebox.showerror("Error","No record found",parent=self.root)
                
         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)


if __name__  =="__main__":                    
    root=Tk()
    obj=ProductClass(root)
    root.mainloop()       