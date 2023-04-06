import sys

import numpy as np
import tkinter
import tkinter.messagebox
import os
import os.path

# 创建应用程序
root = tkinter.Tk()
# 设置窗口的标题
root.title('用户登录界面')
# 设置窗口大小
root['height'] = 300
root['width'] = 600

# 在窗口上创建标签组件（User Name）
# 各个参数的解释：       text设置文本内容    fg='设置字体颜色'    bg='设置字体背景'    font=("设置字体",设置字体大小)    justify=文本标签对齐的方式    anchor='文本对其方式', width=设置的宽度
labeName = tkinter.Label(root, text='用户名:',fg='yellow',bg='purple',font=("微软雅黑",16), justify=tkinter.RIGHT, anchor='e', width=80)
# 显示该组件的位置及大小
labeName.place(x=200, y=50, width=75, height=25)

# 创建字符串变量和文本框组件，同时设置关联的变量
varName = tkinter.StringVar(root, value='')
entryName = tkinter.Entry(root, width=80, textvariable=varName)
entryName.place(x=290, y=50, width=180, height=25)

# 在窗口上创建标签组件（User Pwd）
labeName = tkinter.Label(root, text='密码:',fg='yellow',bg='purple',font=("微软雅黑",16), justify=tkinter.RIGHT, anchor='e', width=80)
# 显示该组件的位置及大小
labeName.place(x=220, y=90, width=55, height=25)

# 创建密码文本框,同时设置关联的变量
varPwd = tkinter.StringVar(root, value='')
entryPwd = tkinter.Entry(root, show='*', width=80, textvariable=varPwd)
entryPwd.place(x=290, y=90, width=180, height=25)



# 登录按钮事件处理函数
def login():
    #file_handle = open('./test.txt', mode='w')
    #file_handle.write("2003050204" + "\n" + "123456")
    #file_handle.flush()
    #file_handle.close()
    # 获取用户名和密码
    name = entryName.get()
    pwd = entryPwd.get()
    with open('test.txt', 'r') as f:
        info = f.read()  # 把文件中的内容读入到info这个内存变量中
        datas = info.split('\n')  # 通过指定分隔符对字符串进行切片
        if name == datas[0] and pwd == datas[1]:
            tkinter.messagebox.showinfo(title='恭喜', message='登录成功！')
        else:
            tkinter.messagebox.showerror('警告', message='用户名或密码错误')
            sys.exit()



# 创建按钮组件，同时设置按钮事件处理函数
# 参数解释：  text='Login'文本内容      activeforeground='#ff0000'按下按钮时文字颜色     command=login关联的函数
buttonOk = tkinter.Button(root, text='登录', activeforeground='#ff0000', command=login)
buttonOk.place(x=160, y=175, width=80, height=25)

# 取消按钮的事件处理函数
def cancel():
#清空用户输入的用户名和密码
    varName.set('')
    varPwd.set('')

buttonCancel = tkinter.Button(root, text='取消', command=cancel)
buttonCancel.place(x=360, y=175, width=80, height=25)

# 启动消息循环
root.mainloop()



