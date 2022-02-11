from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import pymysql
class register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register window")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="black")
        #background image
        self.b=ImageTk.PhotoImage(file="images/bg1.jpg.jpg")
        bg=Label(self.root,image=self.b)
        bg.place(x=250,y=0,relwidth=1,relheight=1)
        #leftbackground image
        self.b1=ImageTk.PhotoImage(file="images/bg4.png")
        bg1=Label(self.root,image=self.b1)
        bg1.place(x=80,y=100,width=400,height=500)

        
        #register frame
        f1=Frame(self.root,bg="white")
        f1.place(x=480,y=100,width=700,height=500)
        t=Label(f1,text="Register here",cursor="hand2",font=("times neew roman",20,"bold"),bg="white",fg="dark blue")
        t.place(x=50,y=30)
        #row1
        fn=Label(f1,text="First name",font=("times neew roman",15,"bold"),bg="white",fg="dark blue")
        fn.place(x=50,y=100)
        self. efn=Entry(f1,font=("times new roman",15),cursor="hand2",bg="light grey")
        self.efn.place(x=50,y=130,width=250)
        ln=Label(f1,text="Last name",font=("times neew roman",15,"bold"),bg="white",fg="dark blue")
        ln.place(x=370,y=100)
        self.eln=Entry(f1,font=("times new roman",15),cursor="hand2",bg="light grey")
        self.eln.place(x=370,y=130,width=250)
        #row2
        cn=Label(f1,text="Contact NO.",font=("times neew roman",15,"bold"),bg="white",fg="dark blue")
        cn.place(x=50,y=170)
        self.ecn=Entry(f1,font=("times new roman",15),cursor="hand2",bg="light grey")
        self.ecn.place(x=50,y=200,width=250)
        em=Label(f1,text="Email",font=("times neew roman",15,"bold"),bg="white",fg="dark blue")
        em.place(x=370,y=170)
        self.eem=Entry(f1,font=("times new roman",15),cursor="hand2",bg="light grey")
        self.eem.place(x=370,y=200,width=250)
        #row3
        ques=Label(f1,text="Securitty Question",font=("times neew roman",15,"bold"),bg="white",fg="dark blue")
        ques.place(x=50,y=240)
        self.cbques=ttk.Combobox(f1,font=("times new roman",13),state="readonly",justify=CENTER)
        self.cbques['values']=["select","your birth place","your favourite food","your pet name"]
        self.cbques.place(x=50,y=270,width=250)
        self.cbques.current(0)
        ans=Label(f1,text="Answer",font=("times neew roman",15,"bold"),bg="white",fg="dark blue")
        ans.place(x=370,y=240)
        self.eans=Entry(f1,font=("times new roman",15),cursor="hand2",bg="light grey")
        self.eans.place(x=370,y=270,width=250)
        pwd=Label(f1,text="Password",font=("times neew roman",15,"bold"),bg="white",fg="dark blue")
        pwd.place(x=50,y=310)
        self.epwd=Entry(f1,font=("times new roman",15),cursor="hand2",bg="light grey")
        self.epwd.place(x=50,y=340,width=250)
        cpwd=Label(f1,text="Confirm Password",font=("times neew roman",15,"bold"),bg="white",fg="dark blue")
        cpwd.place(x=370,y=310)
        self.ecpwd=Entry(f1,font=("times new roman",15),cursor="hand2",bg="light grey")
        self.ecpwd.place(x=370,y=340,width=250)
        #terms
        self.var_chk=IntVar()
        chk=Checkbutton(f1,text="I agree the terms and condition",variable=self.var_chk,onvalue=1,offvalue=0,cursor="hand2",bg="white",font=("times new roman",12))
        chk.place(x=50,y=380)
        btn=Button(f1,text="REGISTER--->",font=("times new roman",12,"bold"),command=self.regis_data,cursor="hand2",bd=0,relief=GROOVE,bg="white",fg="blue")
        btn.place(x=50,y=420)
        btns=Button(self.root,text="Sign In",command=self.login,font=("times new roman",20,"bold"),cursor="hand2",bd=4,relief=GROOVE,bg="blue",fg="white")
        btns.place(x=200,y=460,width=180)
    def clear_data(self):
        self.efn.delete(0,END)
        self.eln.delete(0,END)
        self.ecn.delete(0,END)
        self.eem.delete(0,END)
        self.cbques.current(0)
        self.eans.delete(0,END)
        self.epwd.delete(0,END)
        self.ecpwd.delete(0,END)

    def login(self):
        self.root.destroy()
        import login
    def regis_data(self):
        if self. efn.get()=="" or self. eln.get()=="" or self. ecn.get()=="" or self. eem.get()=="" or self.cbques.get()=="" or self.eans.get()=="" or self.epwd.get()=="" or self.ecpwd.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.epwd.get()!=self.ecpwd.get():
            messagebox.showerror("Error","password and confirm password should be same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","plzzz agree terms and condition",parent=self.root)


        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="emp")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.eem.get())
                r=cur.fetchone()
                if r!=None:
                     messagebox.showerror("Error","user already exist ,plz try with another email",parent=self.root)
                else:
                    cur.execute("insert into employee(fname,lname,contact,email,ques,ans,password)values(%s,%s,%s,%s,%s,%s,%s)",
                    (self. efn.get(),self. eln.get(),self. ecn.get(),self. eem.get(),self.cbques.get(),self.eans.get(),self.epwd.get())) 
                    con.commit()
                    con.close()
                    messagebox.showinfo("Success","registered successfully",parent=self.root)
                    self.clear_data()
            except Exception as es :
                messagebox.showerror("Error",f"error  due to:{str(es)}",parent=self.root)       
               
root=Tk()
ob=register(root)
root.mainloop()