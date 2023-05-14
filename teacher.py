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

    def login():#录入信息
        sql="INSERT INTO info VALUES (?,?,?,?,?,?)"
        if v1.get()!=''and v2.get()!=''and v3.get()!='':
            cu.execute(sql,(v1.get(),v2.get(),v3.get(),v4.get(),v5.get(),v6.get()))
            co.commit()
            tkm.showinfo('提示','录入数据成功')
        else:
            tkm.showerror("错误",'录入失败')
        co.commit()
        
    def Delete():#删除信息
        sql="select id,name,major,c,python,math from info where id='%s'"%v1.get()
        cu.execute(sql)
        s=cu.fetchall()
        if len(s)!=0:
            cu.execute("DELETE FROM info WHERE id='%s'"%v1.get())
            tkm.showinfo("提示",'删除成功')
        else:
            tkm.showerror("删除失败",'学生'+v1.get()+'不存在')
        
        co.commit()

    def update():#修改信息
        cu.execute("select id,name,major,c,python,math from info where id='%s'"%v1.get())
        s=cu.fetchall()
        if len(s)==0:
            tkm.showerror("修改失败",'学生'+v1.get()+'不存在')
        else:
            sql="update info set name='%s',major='%s',c='%s',python='%s',math='%s' where id='%s'"%(v2.get(),v3.get(),v4.get(),v5.get(),v6.get(),v1.get())
            cu.execute(sql)
        co.commit()

    def check():#总览信息
        f=tkFont.Font(size=10)
        sql="select * from info"
        cu.execute(sql)
        s=cu.fetchall()
        r=''
        if len(s)==0:
            tkm.showerror("查阅失败","无学生信息")
        else:
            for k in s:
                r=r+k[0]+','+k[1]+','+k[2]+','+k[3]+','+k[4]+','+k[5]+','+'\n'
        vshow.set(r)
        
    def select():#查询信息
        cu.execute("select id,name,major,c,python,math from info where id='%s'"%v.get())
        s=cu.fetchone() 
        if s==None:
            tkm.showerror("查看失败",'学生'+v1.get()+'不存在')
        else:
            vshow.set(s)

    def tj():
        def px():
            if v1.get()=='C语言'or v1.get()=='C':
                sql="select id,name,major,c from info order by c desc"
                cu.execute(sql)
                s=cu.fetchall()
                r=''
                if len(s)==0:
                    tkm.showerror("查阅失败","无相关成绩信息")
                else:
                    for k in s:
                        r=r+k[0]+','+k[1]+','+k[2]+','+k[3]+'\n'
                vshow.set(r)
            if v1.get()=='Python'or v1.get()=='python':
                sql="select id,name,major,python from info order by python desc"
                cu.execute(sql)
                s=cu.fetchall()
                r=''
                if len(s)==0:
                    tkm.showerror("查阅失败","无相关成绩信息")
                else:
                    for k in s:
                        r=r+k[0]+','+k[1]+','+k[2]+','+k[3]+'\n'
                vshow.set(r)
            if v1.get()=='高数':
                sql="select id,name,major,math from info order by math desc "
                cu.execute(sql)
                s=cu.fetchall()
                r=''
                if len(s)==0:
                    tkm.showerror("查阅失败","无相关成绩信息")
                else:
                    for k in s:
                        r=r+k[0]+','+k[1]+','+k[2]+','+k[3]+'\n'
                vshow.set(r)
            if v1.get()!='高数'and v1.get()!='Python'and v1.get()!='python' and v1.get()!='C语言'and v1.get()!='C':
                tkm.showerror("查阅失败","请重新输入课程")
                
                
        tjym=tk.Toplevel()
        tjym.geometry('520x520')
        tjym.title('排名统计')
        f1=tkFont.Font(family='microsoft yahei',size=20,slant='roman')
        f2=tkFont.Font(family='microsoft yahei',size=14)

        L1=tk.Label(tjym) 
        L1.pack()

        tk.Label(L1,text='成绩排行榜',font=('黑体',20)).grid(row=0,column=0,columnspan=4,sticky='e')

        v1=tk.StringVar()        
        tk.Label(L1,text='课程：',font=f2).grid(row=1,column=0,sticky='w',padx=5,pady=5)
        tk.Entry(L1,textvariable=v1,width=10).grid(row=1,column=1,sticky='w',padx=5,pady=5)

        tk.Button(L1,text='排序',command=px,width=5).grid(row=1,column=2,sticky='w',padx=5,pady=5)
        
        tk.Label(L1,text='学号').grid(row=2,column=0,sticky='w',padx=5,pady=5)
        tk.Label(L1,text='姓名').grid(row=2,column=1,sticky='w',padx=5,pady=5)
        tk.Label(L1,text='专业').grid(row=2,column=2,sticky='w',padx=5,pady=5)
        tk.Label(L1,text='课程成绩').grid(row=2,column=3,sticky='w',padx=5,pady=5)

        L2=tk.Label(tjym,width=500,height=200)
        L2.pack()
        vshow=tk.StringVar()
        tl=tk.Listbox(L2,listvariable=vshow,width=60,height=40).grid(row=1,column=0,sticky='e')



    i=1
    win=tk.Toplevel()
    win.geometry('520x520')
    win.title('成绩管理平台')
    f1=tkFont.Font(family='microsoft yahei',size=20,slant='roman')
    f2=tkFont.Font(family='microsoft yahei',size=14)
    
    L1=tk.Label(win) 
    L1.pack()
            
    tk.Label(L1,text='学生成绩管理平台',font=('黑体',20)).grid(row=0,column=0,columnspan=4,sticky='e')
    
    v1=tk.StringVar()        
    tk.Label(L1,text='学号：',font=f2).grid(row=1,column=0,sticky='w',padx=5,pady=5)
    tk.Entry(L1,textvariable=v1,width=10).grid(row=1,column=1,sticky='w',padx=5,pady=5)

    v2=tk.StringVar()        
    tk.Label(L1,text='姓名：',font=f2).grid(row=2,column=0,sticky='w',padx=5,pady=5)
    tk.Entry(L1,textvariable=v2,width=10).grid(row=2,column=1,sticky='w',padx=5,pady=5)

    v3=tk.StringVar()
    tk.Label(L1,text='专业：',font=f2).grid(row=3,column=0,sticky='w',padx=5,pady=5)
    tk.Entry(L1,textvariable=v3,width=10).grid(row=3,column=1,sticky='w',padx=5,pady=5)

    v4=tk.StringVar()
    tk.Label(L1,text='C语言：',font=f2).grid(row=1,column=2,sticky='w',padx=5,pady=5)
    tk.Entry(L1,textvariable=v4,width=10).grid(row=1,column=3,sticky='w',padx=5,pady=5)

    v5=tk.StringVar()
    tk.Label(L1,text='Python：',font=f2).grid(row=2,column=2,sticky='w',padx=5,pady=5)
    tk.Entry(L1,textvariable=v5,width=10).grid(row=2,column=3,sticky='w',padx=5,pady=5)

    v6=tk.StringVar()
    tk.Label(L1,text='高数：',font=f2).grid(row=3,column=2,sticky='w',padx=5,pady=5)
    tk.Entry(L1,textvariable=v6,width=10).grid(row=3,column=3,sticky='w',padx=5,pady=5)

    tk.Label(L1,text='学号').grid(row=5,column=0,sticky='w',padx=5,pady=5)
    tk.Label(L1,text='姓名').grid(row=5,column=1,sticky='w',padx=5,pady=5)
    tk.Label(L1,text='专业').grid(row=5,column=2,sticky='w',padx=5,pady=5)
    tk.Label(L1,text='C语言').grid(row=5,column=3,sticky='w',padx=5,pady=5)
    tk.Label(L1,text='Python').grid(row=5,column=4,sticky='w',padx=5,pady=5)
    tk.Label(L1,text='高数').grid(row=5,column=5,sticky='w',padx=5,pady=5)
     
    
    tk.Button(L1,text='录入',command=login,width=5).grid(row=4,column=0,sticky='w',padx=5,pady=5)
    tk.Button(L1,text='删除',command=Delete,width=5).grid(row=4,column=1,sticky='w',padx=5,pady=5)
    tk.Button(L1,text='修改',command=update,width=5).grid(row=4,column=2,sticky='w',padx=5,pady=5)
    tk.Button(L1,text='查询',command=select,width=5).grid(row=4,column=3,sticky='w',padx=5,pady=5)
    tk.Button(L1,text='总览',command=check,width=5).grid(row=4,column=4,sticky='w',padx=5,pady=5)
    tk.Button(L1,text='排名',command=tj,width=5).grid(row=4,column=5,sticky='w',padx=5,pady=5)
        
     
    L2=tk.Label(win,width=500,height=200)
    L2.pack()
    vshow=tk.StringVar()
    tl=tk.Listbox(L2,listvariable=vshow,width=60,height=40).grid(row=1,column=0,sticky='e')

    win.mainloop()






        
