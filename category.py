from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class CategoryClass:
     def __init__(self,root):
         self.root=root
         self.root.geometry("1100x500+220+130")
         self.root.title("Inventory management system")
         self.root.config(bg="white")
         self.root.focus_force()
         #######variabels
         self.var_cat_id=StringVar()
         self.var_name=StringVar()
         #### for title
         lbl_title=Label(self.root,text="Manage Category", font=("goudy old style",30),bg="black",fg="violet").pack(side=TOP,fill=X,padx=10,pady=20)
         lbl_name=Label(self.root,text="Enter Category Name",font=("goudy old sty le",30),bg="white").place(x=50,y=100)
         txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",18),bg="lightyellow").place(x=50,y=170 ,width=300)

         btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",14),bg="blue",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
         btn_delete=Button(self.root,text="DELETE",command=self.delete,font=("goudy old style",14),bg="Red",fg="white",cursor="hand2").place(x=520,y=170,width=150,height=30)
         
         ####Category details#################
         cat_frame=Frame(self.root,bd=2,relief=RIDGE)
         cat_frame.place(x=700,y=100,width=380,height=250)

         scrolly=Scrollbar(cat_frame,orient=VERTICAL) 
         scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)    

         self.category_Table=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly,xscrollcommand=scrollx)
         
         scrollx.pack(side=BOTTOM,fill=X)
         scrolly.pack(side=RIGHT,fill=Y)
         scrollx.config(command=self.category_Table.xview)
         scrollx.config(command=self.category_Table.yview)
         

         self.category_Table.heading("cid",text="cid")
         self.category_Table.heading("name",text="NAME")
         self.category_Table["show"]="headings"

         self.category_Table.pack(fill=BOTH,expand=1)
        

         self.category_Table["show"]="headings"

         self.category_Table.column("cid",width=90)
         self.category_Table.column("name",width=100)
         self.category_Table.bind("<ButtonRelease-1>",self.get_data)
#=====================images===========================#
         self.im1=Image.open("cat.jpg")
         self.im1=self.im1.resize((500,200),Image.ANTIALIAS)
         self.im1=ImageTk.PhotoImage(self.im1)

        
         self.lbl_im1=Label(self.root,image=self.im1)
         self.lbl_im1.place(x=50,y=220)
         self.show()
#=====================================btn=====================================================#
     def add(self):
      con=sqlite3.connect(database=r'Inventory.db')
      cur=con.cursor()
      try:
             if self.var_name.get()=="":
                 messagebox.showerror("Error",f"category name must be  required",parent=self.root)
             else:
                 cur.execute("Select * from category where name=?",(self.var_name.get(),))
                 row=cur.fetchone()
                 if row!=None:
                     messagebox.showerror("Error",f"category  already assigned,try with different ID",parent=self.root)
                 else:
                     cur.execute("Insert into category(name)values(?)",(self.var_name.get() ,))    
                     con.commit()
                     messagebox.showinfo("ADD","CATEGORY added sucessfully",parent=self.root)
                     self.show()
      except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
                     #self.show()
#==============show function================#
     def show(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         try:
             cur.execute("select * from category")
             rows=cur.fetchall()
             self.category_Table.delete(*self.category_Table.get_children())
             for row in rows:
                 self.category_Table.insert('',END,values=row)

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)
    
         
     def get_data(self,ev):    
         f=self.category_Table.focus()
         content=(self.category_Table.item(f))
         row=content['values']
         #print(row)
         self.var_cat_id.set(row[0])  
         self.var_name.set(row[1])    

     def delete(self):
         con=sqlite3.connect(database=r'Inventory.db')
         cur=con.cursor()
         try:   
          if self.var_cat_id.get()=="":
                 messagebox.showerror("Error",f"Enter category name",parent=self.root)
          else:
                 cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                 row=cur.fetchone()
                 if row==None:
                     messagebox.showerror("Error",f"category no is invalid",parent=self.root)
                 else:
                     op=messagebox.askyesno("Do you Really want to delete",parent=self.root)
                     if op==True:
                        cur.execute(" Delete from  category  where cid=?",(self.var_cat_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","category Deleted sucessfully",parent=self.root)
                        self.show()
                        self.var_cat_id=''
                        self.var_name=''
                        self.show()

         except Exception as ex:
             messagebox.showerror("Error",f"Error due to {str(ex)}",parent=self.root)            
 






if __name__  =="__main__":                    
    root=Tk()
    obj=CategoryClass(root)
    root.mainloop()        