import sys
import tkinter
import tkinter.messagebox
import sqlite3
import MainRoot
import os
import os.path

class Login():
    def __init__(self):
        #连接数据库
        self.con = sqlite3.Connection('hm_proj.db')
        self.cur = self.con.cursor()
        self.cur.execute("create table if not exists administrator(username varchar(50) primary key, password varchar(50))")
        # 创建应用程序
        self.root = tkinter.Tk()
        # 设置窗口的标题
        self.root.title('用户登录界面')
        # 设置窗口大小
        self.root['height'] = 300
        self.root['width'] = 600

        self.login_success = 0

        # 在窗口上创建标签组件（User Name）
        # 各个参数的解释：       text设置文本内容    fg='设置字体颜色'    bg='设置字体背景'    font=("设置字体",设置字体大小)    justify=文本标签对齐的方式    anchor='文本对其方式', width=设置的宽度
        labeName = tkinter.Label(self.root, text='用户名:',fg='yellow',bg='purple',font=("微软雅黑",16), justify=tkinter.RIGHT, anchor='e', width=80)
        # 显示该组件的位置及大小
        labeName.place(x=200, y=50, width=75, height=25)

        # 创建字符串变量和文本框组件，同时设置关联的变量
        varName = tkinter.StringVar(self.root, value='')
        self.entryName = tkinter.Entry(self.root, width=80, textvariable=varName)
        self.entryName.place(x=290, y=50, width=180, height=25)

        # 在窗口上创建标签组件（User Pwd）
        labeName = tkinter.Label(self.root, text='密码:',fg='yellow',bg='purple',font=("微软雅黑",16), justify=tkinter.RIGHT, anchor='e', width=80)
        # 显示该组件的位置及大小
        labeName.place(x=220, y=90, width=55, height=25)

        # 创建密码文本框,同时设置关联的变量
        varPwd = tkinter.StringVar(self.root, value='')
        self.entryPwd = tkinter.Entry(self.root, show='*', width=80, textvariable=varPwd)
        self.entryPwd.place(x=290, y=90, width=180, height=25)

        # 创建按钮组件，同时设置按钮事件处理函数
        # 参数解释：  text='Login'文本内容      activeforeground='#ff0000'按下按钮时文字颜色     command=login关联的函数
        # 创建登录按钮组件，并设置按钮事件处理函数
        buttonOk = tkinter.Button(self.root, text='登录', activeforeground='#ff0000', command=self.login)
        buttonOk.place(x=160, y=175, width=80, height=25)

        # 创建取消按钮组件，并设置按钮事件处理函数
        buttonCancel = tkinter.Button(self.root, text='取消', command=self.cancel)
        buttonCancel.place(x=360, y=175, width=80, height=25)


    # 启动消息循环
        #self.root.mainloop()

    # 登录按钮事件处理函数
    def login(self):
        #file_handle = open('./test.txt', mode='w')
        #file_handle.write("2003050204" + "\n" + "123456")
        #file_handle.flush()
        #file_handle.close()
        # 获取用户名和密码
        name = self.entryName.get()
        pwd = self.entryPwd.get()
        # 查询数据库，检查用户名和密码是否匹配
        self.cur.execute("SELECT * FROM administrator WHERE username=? AND password=?", (name, pwd))
        result = self.cur.fetchone()
        # 如果查询结果不为空，说明用户名和密码匹配成功
        if result is not None:
            self.login_success = 1
            tkinter.messagebox.showinfo(title='恭喜', message='登录成功！')
        else:
            tkinter.messagebox.showerror('警告', message='用户名或密码错误')
            sys.exit()
        # 关闭数据库连接
        self.con.close()

    # 取消按钮的事件处理函数
    def cancel(self):
    #清空用户输入的用户名和密码
        self.varName.set('')
        self.varPwd.set('')


