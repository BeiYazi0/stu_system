import tkinter as tk
import sqlite3
import tkinter.font as tkFont
import tkinter.messagebox as tkm

def interface():
    
    co=sqlite3.connect("students_info.db")
    cu=co.cursor()
    sql='''create table if not exists info(
id varchar(10) primary key, 
name varchar(10) not null,
major varchar(10) not null ,
c varchar(10) not null,
python varchar(10) not null,
math varchar(10) not null)'''
    co.execute(sql)

    def select():#查询信息
        cu.execute("select id,name,major,c,python,math from info where id='%s'"%v.get())
        s=cu.fetchone() 
        if s==None:
            tkm.showerror("查看失败",'学生'+v1.get()+'不存在')
        else:
            v1.set(s[0])
            v2.set(s[1])
            v3.set(s[2])
            v4.set(s[3])
            v5.set(s[4])
            v6.set(s[5])

    win=tk.Toplevel()
    win.geometry('520x520')
    win.title('成绩查询平台')
    f1=tkFont.Font(family='microsoft yahei',size=20,slant='roman')
    f2=tkFont.Font(family='microsoft yahei',size=14)

    L1=win

    tk.Label(L1,text='学生成绩查询',font=('黑体',20)).place(relx=0.35,rely=0.05)
    
    v=tk.StringVar()        
    tk.Label(L1,text='请输入学号：',font=f2).place(relx=0.15,rely=0.15)
    tk.Entry(L1,textvariable=v,width=10).place(relx=0.4,rely=0.15)
    tk.Label(L1,text='学号：').place(relx=0.2,rely=0.3)
    tk.Label(L1,text='姓名：').place(relx=0.2,rely=0.4)
    tk.Label(L1,text='专业：').place(relx=0.2,rely=0.5)
    tk.Label(L1,text='C语言：').place(relx=0.2,rely=0.6)
    tk.Label(L1,text='Python：').place(relx=0.2,rely=0.7)
    tk.Label(L1,text='高数：').place(relx=0.2,rely=0.8)

    v1=tk.StringVar()        
    tk.Entry(L1,textvariable=v1,width=10).place(relx=0.3,rely=0.3)

    v2=tk.StringVar()        
    tk.Entry(L1,textvariable=v2,width=10).place(relx=0.3,rely=0.4)

    v3=tk.StringVar()
    tk.Entry(L1,textvariable=v3,width=10).place(relx=0.3,rely=0.5)

    v4=tk.StringVar()
    tk.Entry(L1,textvariable=v4,width=10).place(relx=0.3,rely=0.6)

    v5=tk.StringVar()
    tk.Entry(L1,textvariable=v5,width=10).place(relx=0.3,rely=0.7)

    v6=tk.StringVar()
    tk.Entry(L1,textvariable=v6,width=10).place(relx=0.3,rely=0.8)

    

    tk.Button(L1,text='查询',command=select,width=5).place(relx=0.6,rely=0.15)
    L1.mainloop()
    

