import json

import sqlite3
import tkinter as tk
import tkinter.messagebox

import teacher, stu


f = open("info.json", "r", encoding="utf8")
info = json.loads(f.read())
f.close()    

def login():
    user=user_get.get()
    pss=pss_get.get()
    if user in info["users"]:
        h=info["users"].index(user)
        if pss==info["password"][h]:
            if info["type"][h]=="teacher":
                tkinter.messagebox.showinfo("提示","教师登录成功!")
                teacher.interface()
            elif info["type"][h]=="student":
                tkinter.messagebox.showinfo("提示","学生登录成功!")
                stu.interface()
            else:
                tkinter.messagebox.showinfo("提示","管理者登录成功!")
                teacher.interface()
                        
        else:
            tkinter.messagebox.showerror("错误","密码错误!")
                    
    else:
        tkinter.messagebox.showerror("错误","账号不存在!")
            
            
def register():
    zc=tk.Tk()
    zc.title('注册')
    zc.geometry('270x200')
    
    def tj():
        user=zcsrk1.get()
        pss1=zcsrk2.get()
        pss2=zcsrk3.get()
        _type=zcsrk4.get()
        global info
        flag=1
        if user in info["users"]:
            tkinter.messagebox.showerror(title="错误",message="注册失败，账号已被使用")
            flag=0
        if len(pss1)<6:
            tkinter.messagebox.showerror(title="错误",message="注册失败，密码长度不少于6位")
            flag=0
        if pss1 != pss2:
            tkinter.messagebox.showerror(title="错误",message="注册失败，输入的两次密码不一致")
            flag=0
            
        p = {"教师":"teacher","学生":"student"}
        d = p.get(_type)
        if d==None:
            tkinter.messagebox.showerror(title="错误",message="注册失败，请输入教师或者学生")
            flag=0

        if flag==1:
            with open("info.json", 'w', encoding='utf8') as f:
                info["users"].append(user)
                info["password"].append(pss1)
                info["type"].append(d)
                f.write(json.dumps(info, indent=4, ensure_ascii=False))
            tkinter.messagebox.showinfo("提示","注册成功!\n可以进行登录啦！")

         

    zc1=tk.Label(zc,text='账号：')
    zc1.grid(row=1,column=1)
    zcsrk1=tk.Entry(zc)
    zcsrk1.grid(row=1,column=2,pady=10)

    zc2=tk.Label(zc,text='密码：')
    zc2.grid(row=2,column=1,)
    zcsrk2=tk.Entry(zc,show="*")
    zcsrk2.grid(row=2,column=2,pady=10)

    zc3=tk.Label(zc,text='确认密码：')
    zc3.grid(row=3,column=1,)
    zcsrk3=tk.Entry(zc,show="*")
    zcsrk3.grid(row=3,column=2,pady=10)

    zc4=tk.Label(zc,text='用户类型：')
    zc4.grid(row=4,column=1)
    zcsrk4=tk.Entry(zc)
    zcsrk4.grid(row=4,column=2,pady=10)
    tk.Button(zc,text='提交',command=tj).grid(row=5,column=2)
    zc.mainloop()
   
                
       
win=tk.Tk()
win.title('登录')
win.geometry('250x150')

user_get=tk.StringVar()
pss_get=tk.StringVar()

bq1=tk.Label(win,text='账号：')
bq1.place(relx=0.1,rely=0.2)
srk1=tk.Entry(win,textvariable=user_get)
srk1.place(relx=0.25,rely=0.2)

bq2=tk.Label(win,text='密码：')
bq2.place(relx=0.1,rely=0.4)
srk2=tk.Entry(win,textvariable=pss_get,show="*")
srk2.place(relx=0.25,rely=0.4)

tk.Button(win,text='注册',command=register).place(relx=0.3,rely=0.65)
tk.Button(win,text='登录',command=login).place(relx=0.6,rely=0.65)
win.mainloop()

