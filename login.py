from tkinter import*
from PIL import Image,ImageTk
import pymysql
from tkinter import messagebox,ttk
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="violet")

        
         
        lfl=Label(self.root,bg="sky blue",bd=0)
        lfl.place(x=0,y=0,relheight=1,width=600)
        rtl=Label(self.root,bg="dark blue",bd=0)
        rtl.place(x=600,y=0,relheight=1,relwidth=1)

        #frame login
        lgf=Frame(self.root,bg="white")
        lgf.place(x=90,y=120,width=800,height=450)
        title=Label(lgf,text="LOGIN HERE",font=("times new roman",30,"bold"),bg="white",fg="blue")
        title.place(x=400,y=50)
        email=Label(lgf,text="Username",font=("times new roman",15,"bold"),cursor="hand2",bg="white",fg="black")
        email.place(x=400,y=150)
        self.ee=Entry(lgf,font=("times new roman",15,"bold"),cursor="hand2",bg="light grey",fg="black")
        self.ee.place(x=400,y=180,width=350,height=35)
        pwd=Label(lgf,text="Password",font=("times new roman",15,"bold"),cursor="hand2",bg="white",fg="black")
        pwd.place(x=400,y=250)
        self.pe=Entry(lgf,font=("times new roman",15,"bold"),bg="light grey",cursor="hand2",fg="black")
        self.pe.place(x=400,y=280,width=350,height=35)
        regbt=Button(lgf,text="Create new account",command=self.register,font=("times new roman",14),cursor="hand2",bg="white",bd=0,fg="blue")
        regbt.place(x=400,y=320)
        forgetbt=Button(lgf,text="Forget Password",command=self.forget_pwd_window,font=("times new roman",14),cursor="hand2",bg="white",bd=0,fg="red")
        forgetbt.place(x=600,y=320)
        loginbt=Button(lgf,text="Login",command=self.login,font=("times new roman",20,"bold"),cursor="hand2",bg="blue",bd=2,fg="white")
        loginbt.place(x=400,y=360)
        self.b1=ImageTk.PhotoImage(file="images/bg7.png")
        bg1=Label(self.root,image=self.b1,bg="sky blue")
        bg1.place(x=78,y=120,width=350,height=450)
       

    def login(self):
        if self.ee.get()=="" or self.pe.get()=="":
            messagebox.showerror("Error","all fields are required",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="emp")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and password=%s",(self.ee.get(), self.pe.get()))
                r=cur.fetchone()
                if r==None:
                    messagebox.showerror("Error","invalid username & password",parent=self.root)
                else:
                     messagebox.showinfo("Success","Welcome",parent=self.root)
                     self.root.destroy()
                     import pyproject
                con.commit()     
                con.close()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def register(self):
        self.root.destroy()
        import regis
    def fgt_pass(self):
        if self.cbques.get()=="Select" or self.eans.get()=="" or self.enpwd.get()=="":
            messagebox.showerror("Error","All fields ae required",parent=self.win)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="emp")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s and ques=%s and ans=%s",(self.ee.get(),self.cbques.get(),self.eans.get()))
                r=cur.fetchone()
                if r==None:
                    messagebox.showerror("Error","plz select the correct security question/answer",parent=self.win)
                else:
                    cur.execute("update  employee set password=%s where email=%s",(self.enpwd.get(),self.ee.get()))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Succees","your password has been reset plz login with new password",parent=self.win)
                    self.reset()
                    self.win.destroy()

            except Exception as es:
                 messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
    def reset(self):
        self.cbques.current(0)
        self.enpwd.delete(0,END)
        self.eans.delete(0,END)
        self.pe.delete(0,END)
        self.ee.delete(0,END)

    def forget_pwd_window(self):
        if self.ee.get()=="":
            messagebox.showerror("Error","plz enter username or email to reset password",parent=self.root)
        else:
            try:
                con=pymysql.connect(host="localhost",user="root",password="",database="emp")
                cur=con.cursor()
                cur.execute("select * from employee where email=%s",self.ee.get())
                r=cur.fetchone()
                if r==None:
                    messagebox.showerror("Error","plz enter valid username or email to reset password",parent=self.root)
                    
                else:
                    con.commit()
                    con.close()
                    self.win=Toplevel()
                    self.win.title("Forget Password")
                    self.win.geometry("350x400+495+150")
                    self.win.focus_force()
                    self.win.grab_set()
                    t=Label(self.win,text="Forget password",font=("times new roman",20,"bold"),bg="white",fg="red")
                    t.place(x=0,y=10,relwidth=1)
                    self.win.config(bg="white")

         #foget password
                    ques=Label(self.win,text="Securitty Question",font=("times neew roman",15,"bold"),bg="white",fg="dark blue")
                    ques.place(x=50,y=100)
                    self.cbques=ttk.Combobox(self.win,font=("times new roman",13),state="readonly",justify=CENTER)
                    self.cbques['values']=["select","your birth place","your favourite food","your pet name"]
                    self.cbques.place(x=50,y=130,width=250)
                    self.cbques.current(0)
                    ans=Label(self.win,text="Answer",font=("times neew roman",15,"bold"),bg="white",fg="dark blue")
                    ans.place(x=50,y=180)
                    self.eans=Entry(self.win,font=("times new roman",15),cursor="hand2",bg="light grey")
                    self.eans.place(x=50,y=210,width=250)
                    npwd=Label(self.win,text="New Password",font=("times neew roman",15,"bold"),bg="white",fg="dark blue")
                    npwd.place(x=50,y=260)
                    self.enpwd=Entry(self.win,font=("times new roman",15),cursor="hand2",bg="light grey")
                    self.enpwd.place(x=50,y=290,width=250)
                    btn=Button(self.win,text="Reset Pasword",command=self.fgt_pass,bg="green",fg="white",font=("times newv roman",15,"bold"))
                    btn.place(x=90,y=340)

                
                
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)
        

       
root=Tk()
ob=Login(root)       
root.mainloop()