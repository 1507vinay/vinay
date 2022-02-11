from tkinter import*
import pymysql
from tkinter import ttk
from tkinter import messagebox

class student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.configure(background="black")
        self.root.title("Student Management System ")
        p=PhotoImage(file=r"C:\Users\vinay\Downloads\sm.png")
        self.root.iconphoto(False,p)

        t=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",bd=10,relief=GROOVE,font=("times new roman",40,"bold"),bg="dark blue",fg="white")
        t.pack(side=TOP,fill=X)
        self.roll_no_var=StringVar()
        self.name_var=StringVar()
        self.dob_var=StringVar()
        self.email_var=StringVar()
        self.mob_var=StringVar()
        self.gender_var=StringVar()
        self.serach_by=StringVar()
        self.serach_txt=StringVar()
        mf=Frame(self.root,bd=4,relief=RIDGE,bg="dark blue")
        mf.place(x=20,y=100,width=440,height=590)
        df=Frame(self.root,bd=4,relief=RIDGE,bg="dark blue")
        df.place(x=500,y=100,width=830,height=580)
#MANAGE FRAME
        mt=Label(mf,text="Manage Students",bg="dark blue",fg="white",font=("times new roman",30,"bold"))
        mt.grid(row=0,columnspan=2,pady=20)
        lr=Label(mf,text="ROLLNO",bg="dark blue",bd=5,fg="white",font=("times new roman",15,"bold"))
        lr.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        tr=Entry(mf,textvariable=self.roll_no_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
        tr.grid(row=1,column=1,pady=10,padx=20,sticky="w")
        ln=Label(mf,text="Name",bd=5,bg="dark blue",fg="white",font=("times new roman",15,"bold"))
        ln.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        tn=Entry(mf,textvariable=self.name_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
        tn.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        ld=Label(mf,text="D.O.B",bd=5,bg="dark blue",fg="white",font=("times new roman",15,"bold"))
        ld.grid(row=3,column=0,pady=10,padx=20,sticky="w")
        td=Entry(mf,textvariable=self.dob_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
        td.grid(row=3,column=1,pady=10,padx=20,sticky="w")
        le=Label(mf,text="Email",bd=5,bg="dark blue",fg="white",font=("times new roman",15,"bold"))
        le.grid(row=4,column=0,pady=10,padx=20,sticky="w")
        te=Entry(mf,textvariable=self.email_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
        te.grid(row=4,column=1,pady=10,padx=20,sticky="w")
        lm=Label(mf,text="Mob:",bd=5,bg="dark blue",fg="white",font=("times new roman",15,"bold"))
        lm.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        tm=Entry(mf,textvariable=self.mob_var,bd=5,relief=GROOVE,font=("times new roman",15,"bold"))
        tm.grid(row=5,column=1,pady=10,padx=20,sticky="w")
        lg=Label(mf,text="Gender",bd=5,bg="dark blue",fg="white",font=("times new roman",15,"bold"))
        lg.grid(row=6,column=0,pady=10,padx=20,sticky="w")
        cg=ttk.Combobox(mf,textvariable=self.gender_var,font=("times new roman",10,"bold"),state="readonly")
        cg['values']=("Male","Female","Others")
        cg.grid(row=6,column=1,pady=10,padx=20,sticky="w")
        la=Label(mf,text="Address",bd=5,bg="dark blue",fg="white",font=("times new roman",15,"bold"))
        la.grid(row=7,column=0,pady=10,padx=20,sticky="w")
        self.ta=Text(mf,width=26,height=3,font=("times new roman",11,"bold"))
        self.ta.grid(row=7,column=1,pady=10,padx=20,sticky="w")
#button frame
        bf=Frame(mf,bd=4,relief=RIDGE,bg="white")
        bf.place(x=15,y=500,width=410)
        ab=Button(bf,text="Add",width=10,bd=3,bg="dark blue",fg="white",relief=GROOVE,command=self.add_stud)
        ab.grid(row=0,column=0,padx=10,pady=10)
        ub=Button(bf,text="Update",bg="dark blue",fg="white",command=self.update_data,width=10,bd=3,relief=GROOVE)
        ub.grid(row=0,column=1,padx=10,pady=10)
        db=Button(bf,text="Delete",bg="dark blue",fg="white",command=self.delete_data,width=10,bd=3,relief=GROOVE)
        db.grid(row=0,column=2,padx=10,pady=10)
        cb=Button(bf,text="Clear",bg="dark blue",fg="white",command=self.clear,width=10,bd=3,relief=GROOVE)
        cb.grid(row=0,column=3,padx=10,pady=10)
#DETAIL FRAME
        ls=Label(df,text="Search By",bg="dark blue",fg="white",font=("times new roman",20,"bold"))
        ls.grid(row=0,column=0,padx=20,pady=10)
        cs=ttk.Combobox(df,width=10,textvariable=self.serach_by,font=("times new roman",10,"bold"),state="readonly")
        cs['values']=("Select option","rollno","NAME","CONTACTS")
        cs.grid(row=0,column=1,pady=20,padx=30,sticky="w")
        cs.current(0)

        es=Entry(df,width=18,textvariable=self.serach_txt,bd=5,font=("times new roman",15,"bold"))
        es.grid(row=0,column=2,pady=10,padx=20,sticky="w")
        sb=Button(df,text="Search",fg="white",bg="dark blue",command=self.search_data,width=12,bd=3)
        sb.grid(row=0,column=3,padx=10,pady=10)
        sab=Button(df,text="Show All",fg="white",bg="dark blue",command=self.fetch_data,width=12,bd=3)
        sab.grid(row=0,column=4,padx=10,pady=10)
# table frame
        tf=Frame(df,bd=4,relief=RIDGE,bg="white")
        tf.place(x=10,y=70,width=780,height=490)
        sbx=Scrollbar(tf,orient=HORIZONTAL)
        sby=Scrollbar(tf,orient=VERTICAL)
        self.data_Treeview=ttk.Treeview(tf,show='headings',column=('ROLLNO','NAME','DOB','EMAIL',"MOB","GENDER","ADDRESS"),
        xscrollcommand=sbx.set,yscrollcommand=sby.set)
        sbx.pack(side=BOTTOM,fill=X)
        sby.pack(side=RIGHT,fill=Y)
        sbx.config(command=self.data_Treeview.xview)
        sby.config(command=self.data_Treeview.yview)
        self.data_Treeview.column('ROLLNO',width=150,anchor="center")
        self.data_Treeview.column('NAME',width=150,anchor="center")
        self.data_Treeview.column('DOB',width=150,anchor="center")
        self.data_Treeview.column('EMAIL',width=150,anchor="center")
        self.data_Treeview.column('MOB',width=150,anchor="center")
        self.data_Treeview.column('GENDER',width=150,anchor="center")
        self.data_Treeview.column('ADDRESS',width=150,anchor="center")


        self.data_Treeview.heading('ROLLNO',text='ROLLNO')
        self.data_Treeview.heading('NAME',text='NAME')
        self.data_Treeview.heading('DOB',text='DOB')
        self.data_Treeview.heading('EMAIL',text='EMAIL')
        self.data_Treeview.heading('MOB',text='MOB')
        self.data_Treeview.heading('GENDER',text='GENDER')
        self.data_Treeview.heading('ADDRESS',text='ADDRESS')
        self.data_Treeview.pack()
        self.data_Treeview.bind("<ButtonRelease-1>",self.get_cursor)
        
       
        
    def add_stud(self):
            if self.roll_no_var.get()=="" or self.name_var.get()=="":
                    messagebox.showerror("error","all fields are required!")
            else:
                    con=pymysql.connect(host="localhost",user="root",password="",database="cms")
                    cur=con.cursor()
                    cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.roll_no_var.get(),
                                                                                     self.name_var.get(),
                                                                                     self.dob_var.get(),
                                                                                     self.email_var.get(),
                                                                                     self.mob_var.get(),
                                                                                     self.gender_var.get(),
                                                                                     self.ta.get('1.0',END
                                                                                     )))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("succes","record has been inserted")
    def fetch_data(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="cms")
            cur=con.cursor()
            cur.execute("select * from students")
            row=cur.fetchall()
            if len(row)!=0:
                    self.data_Treeview.delete(*self.data_Treeview.get_children())
                    for i in row:
                            self.data_Treeview.insert('',END,values=i)
                    con.commit()
            con.close()        

    def clear(self):
            self.roll_no_var.set("")
            self.name_var.set("")
            self.dob_var.set("")
            self.email_var.set("")
            self.mob_var.set("")
            self.gender_var.set("")
            self.ta.delete('1.0',END)

    def get_cursor(self,ev):
            cr=self.data_Treeview.focus()
            c=self.data_Treeview.item(cr)
            r=c['values']
            self.roll_no_var.set(r[0])
            self.name_var.set(r[1])
            self.dob_var.set(r[2])
            self.email_var.set(r[3])
            self.mob_var.set(r[4])
            self.gender_var.set(r[5])
            self.ta.delete('1.0',END)
            self.ta.insert(END,r[6])

    def update_data(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="cms")
            cur=con.cursor()
            cur.execute("update students set name=%s,dob=%s,email=%s,gender=%s,mob=%s,address=%s where rollno=%s",(
                                                                                               self.name_var.get(),
                                                                                               self.dob_var.get(),
                                                                                               self.email_var.get(),
                                                                                               self.mob_var.get(),
                                                                                               self.gender_var.get(),
                                                                                               self.ta.get('1.0',END),
                                                                                               self.roll_no_var.get()
                                                                                               ))

            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
    def delete_data(self):
             con=pymysql.connect(host="localhost",user="root",password="",database="cms")
             cur=con.cursor()
             cur.execute("delete from students where rollno=%s",self.roll_no_var.get())
             con.commit()
             con.close()
             self.fetch_data()
             self.clear()
    def search_data(self):
            con=pymysql.connect(host="localhost",user="root",password="",database="cms")
            cur=con.cursor()
            cur.execute("select * from students where "+str(self.serach_by.get()) + " LIKE '%"+str(self.serach_txt.get())+"%'")
            row=cur.fetchall()
            if len(row)!=0:
                    self.data_Treeview.delete(*self.data_Treeview.get_children())
                    for i in row:
                            self.data_Treeview.insert('',END,values=i)
                    con.commit()
            con.close()      
root=Tk()
ob=student(root)
root.mainloop()
