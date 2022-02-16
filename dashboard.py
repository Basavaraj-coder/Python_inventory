from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import SupplierClass
from category import CategoryClass
from product import ProductClass 
from sales import salesClass

class IMS:
    def __init__(self,root):
         self.root=root
         self.root.geometry("1350x800+0+0")
         self.root.title("Inventory management system")
         bg_color="#074463"
         self.root.title("Inventory Management System | Developed by Basavaraj Hiremath") 
         title=Label(self.root,text="Inventory Management System", font=("Times new Roman",40,"bold"),bg="#010c48",fg="pink").place(x=0,y=0,relwidth=1,height=70)
         #===btn_signout===#

        #  btn_logout=Button(self.root,text="Sign Out",font=("Times new Roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1200,y=10,height=50,width=170)
         self.lbl_clock=Label(self.root,text=" Welcome To Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time:HH:MM:SS", font=("times new Roman",12,"bold"),bg="grey",fg="white")         
         self.lbl_clock.place(x=0,y=70,relwidth=1,height=27)  
        #====left menu====#
         self.MenuLogo=Image.open("optlogo.png")
         self.MenuLogo=self.MenuLogo.resize((150,150),Image.ANTIALIAS)
         self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

         LeftMenu=Frame(self.root,bd=2,relief=RIDGE)
         LeftMenu.place(x=2,y=100,width=200,height=600)
         
         lbl_menuLogo=Label(LeftMenu,image=self.MenuLogo)
         lbl_menuLogo.pack(side=TOP,fill=X)

         lbl_menu=Label(LeftMenu, text= " Menu ", font=("times new roman",30,"bold"),bg="white",bd=3).pack(side=TOP,fill=X)

         #self.icon_side=PhotoImage(file="optlogo.png")
         btn_employee=Button(LeftMenu,text="Employee",command=self.employee,font=("times new roman",24,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X) 
         btn_employee=Button(LeftMenu,text="Supplier",command=self.Supplier,font=("times new roman",24,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X) 
         btn_employee=Button(LeftMenu,text="Category",command=self.category,font=("times new roman",24,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
         btn_employee=Button(LeftMenu,text="Products",command=self.product,font=("times new roman",24,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
         btn_employee=Button(LeftMenu,text="Sales", command=self.sales,font=("times new roman",24,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
         btn_employee=Button(LeftMenu,text="Exit",font=("times new roman",24,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
         #====content=====#
         self.lbl_employee=Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="orange",fg="white",font=("times new roman",20,"bold"))
         self.lbl_employee.place(x=300,y=120,height=150,width=200)

         self.lbl_supplier=Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="violet",fg="white",font=("times new roman",20,"bold"))
         self.lbl_supplier.place(x=600,y=120,height=150,width=200)

         self.lbl_category=Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="black",fg="white",font=("times new roman",20,"bold"))
         self.lbl_category.place(x=950,y=120,height=150,width=200)

         self.lbl_products=Label(self.root,text="Total Products\n[ 0 ]",bd=5,relief=RIDGE,bg="Green",fg="white",font=("times new roman",20,"bold"))
         self.lbl_products.place(x=300,y=300,height=150,width=200)

         self.lbl_sales=Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="red",fg="white",font=("times new roman",20,"bold"))
         self.lbl_sales.place(x=600,y=300,height=150,width=200)

         #====Bottom-----#
         lbl_footer=Label(self.root,text="Inventory Management System | Developed By Basavaraj Hiremath,for any queries Contact 8956651905",font=("times new Roman",12,"bold"),bg="grey",fg="white").pack(side=BOTTOM,fill=X)       
         #=======
    def employee(self):
             self.new_win=Toplevel(self.root)
             self.new_obj=employeeClass(self.new_win)
    def Supplier(self):
             self.new_win=Toplevel(self.root)
             self.new_obj=SupplierClass(self.new_win)
    def category(self):
             self.new_win=Toplevel(self.root)
             self.new_obj=CategoryClass(self.new_win)
    def product(self):
             self.new_win=Toplevel(self.root)
             self.new_obj=ProductClass(self.new_win)
    def sales(self):
             self.new_win=Toplevel(self.root)
             self.new_obj=salesClass(self.new_win)

if __name__  =="__main__":                    
    root=Tk()
    obj=IMS(root)
    root.mainloop()       