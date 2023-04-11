from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
from PIL import ImageTk,Image
import os
import sqlite3
import login_system
import  sys
import MainRoot


now = datetime.datetime.now()


#-------------import sqlite for server side operations and create table---------------------------------------------------------------------------------
con = sqlite3.Connection('hm_proj.db')
cur = con.cursor()
# cur.execute("delete from paymentsf")
# cur.execute("INSERT INTO paymentsf VALUES(0,'test','test1','NULL','@NULL','NULL','21','Nov','2022','19:19','NULL',0)")
cur.execute("create table if not exists hoteld(t_r number,r_r number,t_s number)")
cur.execute("create table if not exists roomd(rn number primary key,beds number,ac varchar(10),tv varchar(10),internet varchar(10),price number(10))")
cur.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar,totalamt varchar)")
# cur.execute("create table if not exists payments(id number primary key,dot varchar(15),time varchar(10),amt number,method varchar(10))")

con.commit()
con.commit()
# cur.execute("select * from payments")
con.commit()
x=cur.fetchall()
con.commit()


#-----------启动画面------------------------------------------------------------------------------------------------------------------
def start():
    sroot = Tk()
    sroot.title("启动中")
    sroot.minsize(height=516,width=1150)

    spath = "images/cover.jpg"
    simg = ImageTk.PhotoImage(Image.open(spath))
    my = Label(sroot,image=simg)
    my.image = simg
    my.place(x=0,y=0)


    Label(sroot,text="欢迎进入",font='Timesnewroman 40 ',fg='black').place(x=635,y=250)
    Label(sroot,text="STARRY ",font='Timesnewroman 50 ',fg='pink').place(x=435,y=320)
    Label(sroot,text="酒店管理系统 ",font='Timesnewroman 50 ',fg='black').place(x=650,y=320)
    Label(sroot,text="组员：张泽西，臧元祥",font='Timesnewroman 20 ',fg='grey').place(x=535,y=420)

    sroot.after(3000, lambda: sroot.destroy())
    sroot.mainloop()

#----------- 项目主体------------------------------------------------------------------------------------------------------------------
def mainroot():
    root = Tk()
    root.geometry('1080x500')
    root.minsize(width=1080, height=550)
    root.maxsize(width=1080, height=550)
    root.configure(bg='white')
    root.title("酒店管理系统v1.1.2")

    # --------------分割-------------------------------------------------------------------------------------------------------------------

    sep = Frame(height=500, bd=1, relief='sunken', bg='white')

    # ----------------连接printer-------------------------------------------------------------------------------------------------------------

    def connectprinter():
        os.startfile("test.txt", "print")

    # ---------------顶框------------------------------------------------------------------------------------------------------------------

    top_frame = Frame(root, height=70, width=1080, bg='orange')
    path = "images/background1.jpg"
    img = ImageTk.PhotoImage(Image.open(path))
    label = Label(top_frame, image=img, height=70, width=1080)
    label.image = img
    label.place(x=0, y=0)
    top_frame.place(x=0, y=0)
    tf_label = Label(top_frame, text='酒店管理系统', font='msserif 33', fg='black', bg='gray89', height=70)
    tf_label.pack(anchor='center')
    top_frame.pack_propagate(False)

    # ---------------DATE TIME------------------------------------------------------------------------------------------------------------------
    def datetime():
        # while(True):
        localtime = now.strftime("%Y-%m-%d %H:%M")
        lblInfo = Label(top_frame, font='helvetica 15', text=localtime, bg='blue', fg='white')

    # lblInfo.place(x=333,y=40)

    # ----------------底框 - 基础和默认页-------------------------------------------------------------------------------
    def hotel_status():
        global b_frame
        b_frame = Frame(root, height=400, width=1080, bg='gray91')
        b_frame.place(x=0, y=120 + 6 + 20 + 60 + 11)
        b_frame.pack_propagate(False)
        path = "images/background2.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(b_frame, image=img, height=400, width=1080)
        label.image = img
        label.place(x=0, y=0)
        cur.execute("select * from hoteld")
        x = cur.fetchall()
        cur.execute("select count(rn) from roomd")
        x = cur.fetchone()

        cur.execute("select count(rn) from roomd where rstatus = 'Reserved'")
        y = cur.fetchone()

        tor = x[0]
        rer = y[0]
        tos = 4
        avr = int(tor) - int(rer)
        avr = str(avr)
        hts = Label(b_frame, text='酒店明细', font='msserif 60', fg='black', bg='gray91', height=1)
        # ------------内框和底框-------------------------

        smf1 = Frame(b_frame, height=150, width=175, bg='white')
        tr = Label(smf1, text='总房间数:', fg='white', bg='cyan4', width=100, height=2, font='helvetica 15')
        tr.pack(side='top')
        smf1.pack_propagate(False)
        smf1.place(x=0, y=60)
        Label(smf1, text=tor, fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')

        smf2 = Frame(b_frame, height=150, width=175, bg='white')
        ar = Label(smf2, text='空闲房间数:', fg='white', bg='cyan4', width=130, height=2, font='helvetica 15')
        ar.pack(side='top')
        smf2.pack_propagate(False)
        smf2.place(x=180 + 4, y=60)
        Label(smf2, text=avr, fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')

        smf3 = Frame(b_frame, height=150, width=175, bg='white')
        tre = Label(smf3, text='总预定数:', fg='white', bg='cyan4', width=130, height=2, font='helvetica 15')
        tre.pack(side='top')
        smf3.pack_propagate(False)
        smf3.place(x=360 + 6, y=60)
        Label(smf3, text=rer, fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')

        # ------------------可视化：总顾客人数-----------------------------------------未完成
        # 未完成--------------------------------------------------
        smf4 = Frame(b_frame, height=150, width=175, bg='white')
        tc = Label(smf4, text='总顾客数:', fg='white', bg='cyan4', width=130, height=2, font='helvetica 15')
        tc.pack(side='top')
        smf4.pack_propagate(False)
        smf4.place(x=540 + 8, y=60)
        Label(smf4, text='0', fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')
        # ------------------------------------------------------------------

        smf5 = Frame(b_frame, height=150, width=175, bg='white')
        ts = Label(smf5, text='总职员数:', fg='white', bg='cyan4', width=130, height=2, font='helvetica 15')
        ts.pack(side='top')
        smf5.pack_propagate(False)
        smf5.place(x=720 + 10, y=60)
        Label(smf5, text=tos, fg='cyan4', bg='white', font='msserif 50').pack(anchor='center')
        redf1 = Frame(b_frame, height=8, width=1080, bg='cyan4')

        smf6 = Frame(b_frame, height=150, width=175, bg='white')
        ts = Label(smf6, text='装修中的房间数:', fg='white', bg='cyan4', width=130, height=2, font='helvetica 15')
        ts.pack(side='top')
        smf6.pack_propagate(False)
        smf6.place(x=915, y=60)
        Label(smf6, text='3', fg='cyan4', bg='white', font='msserif 50').place(x=60, y=60)
        # redf1 = Frame(b_frame,height=8,width=1080,bg='cyan4')

        # Label(b_frame,text='==================================================================================',fg='cyan4').place(x=0,y=20)
        redf1.place(x=0, y=22)
        Label(b_frame, text='酒店明细', font='msserif 30', bg='cyan4', fg='white').pack(anchor='center')
        redf1.pack_propagate(False)
        # b_frame.pack_propagate(False)

        # -----------------------------------------------------------------
        nl = Label(b_frame, text='组员：张泽西、臧元祥', fg='black', bg='gray91', font='msserif 8')
        nl.place(x=855, y=310)
        nl.tkraise()

    # -------------- Guests --------------------------------------------------------------------------------------------------------------------------
    def staff():
        b_frame = Frame(root, height=400, width=1080, bg='white')
        path = "images/background2.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(b_frame, image=img, height=400, width=1080)
        label.image = img
        label.place(x=0, y=0)
        # 1
        emp1f = Frame(b_frame)
        path1 = "images/Nijika.jpg"
        img1 = ImageTk.PhotoImage(Image.open(path1))
        emp1 = Label(emp1f, image=img1)
        emp1.image = img1
        emp1.pack()
        emp1f.place(x=50, y=0)
        emp1inf = Frame(b_frame, bg='White', height=120, width=300)
        Label(emp1inf, text="总经理", bg='white', font='msserif 17 bold').place(x=30, y=5)
        Label(emp1inf, text="伊地知虹夏", bg='white', font='msserif 14 ').place(x=30, y=37)
        Label(emp1inf, text="电话 : 002", bg='white', fg="Grey", font='msserif 12').place(x=30, y=61)
        Label(emp1inf, text="邮箱 : Nijika@StarryHotel.com", bg='white', fg="Grey", font='msserif 12').place(x=30, y=83)
        emp1inf.pack_propagate(False)
        emp1inf.place(x=180, y=1)
        # 2
        emp1f = Frame(b_frame)
        path2 = "images/Ryo.jpg"
        img2 = ImageTk.PhotoImage(Image.open(path2))
        emp1 = Label(emp1f, image=img2)
        emp1.image = img2
        emp1.pack()
        emp1f.place(x=580, y=0)
        emp1inf = Frame(b_frame, bg='White', height=120, width=300)
        Label(emp1inf, text="总经办", bg='white', font='msserif 17 bold').place(x=45, y=5)
        Label(emp1inf, text="山田凉", bg='white', font='msserif 14 ').place(x=45, y=37)
        Label(emp1inf, text="电话 : 005", bg='white', fg="Grey", font='msserif 12').place(x=45, y=61)
        Label(emp1inf, text="邮箱 : Ryo@StarryHotel.com", bg='white', fg="Grey", font='msserif 12').place(x=45, y=83)
        emp1inf.pack_propagate(False)
        emp1inf.place(x=700, y=2)
        # 3
        emp1f = Frame(b_frame)
        path3 = "images/Hitori.jpg"
        img3 = ImageTk.PhotoImage(Image.open(path3))
        emp1 = Label(emp1f, image=img3)
        emp1.image = img3
        emp1.pack()
        emp1f.place(x=50, y=152)
        emp1inf = Frame(b_frame, bg='White', height=120, width=300)
        Label(emp1inf, text="餐饮部（领班）", bg='white', font='msserif 17 bold').place(x=30, y=5)
        Label(emp1inf, text="后藤一里", bg='white', font='msserif 14 ').place(x=30, y=37)
        Label(emp1inf, text="电话 : 007", bg='white', fg="Grey", font='msserif 12').place(x=30, y=61)
        Label(emp1inf, text="邮箱 : Hitori@StarryHotel.com", bg='white', fg="Grey", font='msserif 12').place(x=30, y=83)
        emp1inf.pack_propagate(False)
        emp1inf.place(x=180, y=153)
        emp1inf.tkraise()
        # 4
        emp1f = Frame(b_frame)
        path4 = "images/Ikuyo.jpg"
        img4 = ImageTk.PhotoImage(Image.open(path4))
        emp1 = Label(emp1f, image=img4)
        emp1.image = img4
        emp1.pack()
        emp1f.place(x=580, y=152)
        emp1inf = Frame(b_frame, bg='White', height=120, width=300)
        Label(emp1inf, text="客房服务（领班）", bg='white', font='msserif 17 bold').place(x=45, y=5)
        Label(emp1inf, text="喜多郁代", bg='white', font='msserif 14 ').place(x=45, y=37)
        Label(emp1inf, text="电话 : 011", bg='white', fg="Grey", font='msserif 12').place(x=45, y=61)
        Label(emp1inf, text="邮箱 : Ikuyo@StarryHotel.com", bg='white', fg="Grey", font='msserif 12').place(x=45, y=83)
        emp1inf.pack_propagate(False)
        emp1inf.place(x=700, y=153)

        b_frame.place(x=0, y=120 + 6 + 20 + 60 + 11)
        b_frame.pack_propagate(False)
        b_frame.tkraise()
        nl = Label(b_frame, text='组员：张泽西、臧元祥', fg='black', font='msserif 8')
        nl.place(x=855, y=310)
        nl.tkraise()

    # -------------- 房间 --------------------------------------------------------------------------------------------------------------------------
    def rooms():
        b_frame = Frame(root, height=400, width=1080, bg='gray91')
        b_frame.place(x=0, y=120 + 6 + 20 + 60 + 11)
        b_frame.pack_propagate(False)
        b_frame.tkraise()
        path = "images/background2.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(b_frame, image=img, height=400, width=1080)
        label.image = img
        label.place(x=0, y=0)
        sidebuttons = Text(b_frame, width=1, height=19)
        sc = Scrollbar(b_frame, command=sidebuttons.yview, width=10, bg='lightsteelblue3')
        sidebuttons.configure(yscrollcommand=sc.set)
        sc.pack(side='left', fill=Y)
        sidebuttons.place(x=10, y=0)

        def roomdet(rno):
            Label(b_frame, text='房间 %s' % rno, font='msserif 15', fg='white', bg='cyan4', width=10).place(x=535, y=0)
            cur.execute("select * from roomd where rn = ?", (rno,))
            rdata = cur.fetchall()
            smf1 = Frame(b_frame, height=120, width=145, bg='white')
            hline = Frame(b_frame, height=10, width=960, bg='cyan4')
            hline.place(x=120, y=27)
            vline = Frame(b_frame, height=400, width=7, bg='lightsteelblue3')
            vline.place(x=120, y=0)
            tr = Label(smf1, text='总床数:', fg='white', bg='cyan4', width=100, height=2, font='msserif 15')
            tr.pack(side='top')
            smf1.pack_propagate(False)
            smf1.place(x=130, y=30)
            Label(smf1, text=str(rdata[0][1]), fg='cyan4', bg='white', font='msserif 35').pack()
            smf2 = Frame(b_frame, height=120, width=145, bg='white')
            tr = Label(smf2, text='网线', fg='white', bg='cyan4', width=100, height=2, font='msserif 15')
            tr.pack(side='top')
            smf2.pack_propagate(False)
            smf2.place(x=290, y=30)
            Label(smf2, text=str(rdata[0][2]), fg='cyan4', bg='white', font='msserif 35').pack()
            smf2 = Frame(b_frame, height=120, width=145, bg='white')
            tr = Label(smf2, text='电视机', fg='white', bg='cyan4', width=100, height=2, font='msserif 15')
            tr.pack(side='top')
            smf2.pack_propagate(False)
            smf2.place(x=450, y=30)
            Label(smf2, text=str(rdata[0][3]), fg='cyan4', bg='white', font='msserif 35').pack()
            smf2 = Frame(b_frame, height=120, width=145, bg='white')
            tr = Label(smf2, text=' Wifi', fg='white', bg='cyan4', width=100, height=2, font='msserif 15')
            tr.pack(side='top')
            smf2.pack_propagate(False)
            smf2.place(x=610, y=30)
            Label(smf2, text=str(rdata[0][4]), fg='cyan4', bg='white', font='msserif 35').pack()
            smf2 = Frame(b_frame, height=120, width=145, bg='white')
            tr = Label(smf2, text=' 价格￥/晚', fg='white', bg='cyan4', width=100, height=2, font='msserif 15')
            tr.pack(side='top')
            smf2.pack_propagate(False)
            smf2.place(x=770, y=30)
            Label(smf2, text=str(rdata[0][5]), fg='cyan4', bg='white', font='msserif 35').pack()
            smf2 = Frame(b_frame, height=120, width=145, bg='white')
            tr = Label(smf2, text='预定状态', fg='white', bg='cyan4', width=100, height=2, font='msserif 15')
            tr.pack(side='top')
            smf2.pack_propagate(False)
            smf2.place(x=930, y=30)
            p = ''
            if rdata[0][6] == 'Unreserved':
                p = '  空闲'
            else:
                p = '已被预定'
            Label(smf2, text=p, fg='cyan4', bg='white', font='msserif 25').place(x=0, y=55)

        roomdet(1)

        sidebuttons.configure(state='disabled')
        b1 = Button(b_frame, font='mssherif 10', text="房间 1", bg='white', fg='cyan4', width=10,
                    command=lambda: roomdet(1))
        b2 = Button(b_frame, font='mssherif 10', text="房间 2", bg='white', fg='cyan4', width=10,
                    command=lambda: roomdet(2))
        b3 = Button(b_frame, font='mssherif 10', text="房间 3", bg='white', fg='cyan4', width=10,
                    command=lambda: roomdet(3))
        b4 = Button(b_frame, font='mssherif 10', text="房间 4", bg='white', fg='cyan4', width=10,
                    command=lambda: roomdet(4))
        b5 = Button(b_frame, font='mssherif 10', text="房间 5", bg='white', fg='cyan4', width=10,
                    command=lambda: roomdet(5))
        b6 = Button(b_frame, font='mssherif 10', text="房间 6", bg='white', fg='cyan4', width=10,
                    command=lambda: roomdet(6))
        b7 = Button(b_frame, font='mssherif 10', text="房间 7", bg='white', fg='cyan4', width=10,
                    command=lambda: roomdet(7))
        b8 = Button(b_frame, font='mssherif 10', text="房间 8", bg='white', fg='cyan4', width=10,
                    command=lambda: roomdet(8))
        b9 = Button(b_frame, font='mssherif 10', text="房间 9", bg='white', fg='cyan4', width=10,
                    command=lambda: roomdet(9))
        b10 = Button(b_frame, font='mssherif 10', text="房间 10", bg='white', fg='cyan4', width=10,
                     command=lambda: roomdet(10))
        b11 = Button(b_frame, font='mssherif 10', text="房间 11", bg='white', fg='cyan4', width=10,
                     command=lambda: roomdet(11))
        b12 = Button(b_frame, font='mssherif 10', text="房间 12", bg='white', fg='cyan4', width=10,
                     command=lambda: roomdet(12))
        b13 = Button(b_frame, font='mssherif 10', text="房间 13", bg='white', fg='cyan4', width=10,
                     command=lambda: roomdet(13))
        b14 = Button(b_frame, font='mssherif 10', text="房间 14", bg='white', fg='cyan4', width=10,
                     command=lambda: roomdet(14))
        b15 = Button(b_frame, font='mssherif 10', text="房间 15", bg='white', fg='cyan4', width=10,
                     command=lambda: roomdet(15))
        b16 = Button(b_frame, font='mssherif 10', text="房间 16", bg='white', fg='cyan4', width=10,
                     command=lambda: roomdet(16))
        b17 = Button(b_frame, font='mssherif 10', text="房间 17", bg='white', fg='cyan4', width=10,
                     command=lambda: roomdet(17))
        b18 = Button(b_frame, font='mssherif 10', text="房间 18", bg='white', fg='cyan4', width=10,
                     command=lambda: roomdet(18))
        b19 = Button(b_frame, font='mssherif 10', text="房间 19", bg='white', fg='cyan4', width=10,
                     command=lambda: roomdet(19))
        b20 = Button(b_frame, font='mssherif 10', text="房间 20", bg='white', fg='cyan4', width=10,
                     command=lambda: roomdet(20))
        sidebuttons.window_create("end", window=b1)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b2)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b3)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b4)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b5)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b6)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b7)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b8)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b9)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b10)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b11)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b12)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b13)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b14)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b15)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b16)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b17)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b18)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b19)
        sidebuttons.insert("end", "\n")
        sidebuttons.window_create("end", window=b20)
        nl = Label(b_frame, text='组员：张泽西、臧元祥', fg='black', bg='gray91', font='msserif 8')
        nl.place(x=855, y=310)
        nl.tkraise()

    # --------------- 支付方式-----------------------------------------------------------------------------------------------------------------------

    def payments():
        b_frame = Frame(root, height=400, width=1080, bg='gray89')
        path = "images/background2.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(b_frame, image=img, height=400, width=1080)
        label.image = img
        label.place(x=0, y=0)
        l = Label(b_frame, text='请输入交易ID', font='msserif 15', bg='cyan4', fg='white')
        l.place(x=245, y=0)
        b_frame.place(x=0, y=120 + 6 + 20 + 60 + 11)
        b_frame.pack_propagate(False)
        b_frame.tkraise()
        hline = Frame(b_frame, height=42, width=1080, bg='cyan4')
        hline.place(x=0, y=23)
        ef = Frame(hline)
        p_id = Entry(ef)
        p_id.pack(ipadx=25, ipady=3)
        ef.place(x=308, y=6)

        fl1 = Frame(b_frame, height=38, width=308, bg='cyan4')
        fl1.place(x=0, y=68)
        l1 = Label(fl1, text='办理日期', bg='cyan4', fg='white', font='msserif 17')
        l1.pack()
        fl1.pack_propagate(False)

        fr1 = Frame(b_frame, height=38, width=1080 - 308, bg='white')
        fr1.place(x=0 + 308, y=68)
        l1 = Label(fl1, text='办理日期', bg='cyan4', fg='white', font='msserif 17')
        # l1.pack()
        fr1.pack_propagate(False)

        fl2 = Frame(b_frame, height=38, width=308, bg='cyan4')
        fl2.place(x=0, y=109)
        fl2.pack_propagate(False)
        l1 = Label(fl2, text='办理时间', bg='cyan4', fg='white', font='msserif 17')
        l1.pack()

        fr2 = Frame(b_frame, height=38, width=1080 - 308, bg='white')
        fr2.place(x=0 + 308, y=109)
        fr2.pack_propagate(False)
        l1 = Label(fl1, text='办理日期', bg='cyan4', fg='white', font='msserif 17')
        # l1.pack()

        fl3 = Frame(b_frame, height=38, width=308, bg='cyan4')
        fl3.place(x=0, y=150)
        fl3.pack_propagate(False)
        l1 = Label(fl3, text='总支付金额', bg='cyan4', fg='white', font='msserif 17')
        l1.pack()

        fr3 = Frame(b_frame, height=38, width=1080 - 308, bg='white')
        fr3.place(x=0 + 308, y=150)
        fr3.pack_propagate(False)
        l1 = Label(fl1, text='办理日期', bg='cyan4', fg='white', font='msserif 17')
        # l1.pack()

        fl4 = Frame(b_frame, height=38, width=308, bg='cyan4')
        fl4.place(x=0, y=191)
        fl4.pack_propagate(False)
        l1 = Label(fl4, text='支付方式', bg='cyan4', fg='white', font='msserif 17')
        l1.pack()

        fr4 = Frame(b_frame, height=38, width=1080 - 308, bg='white')
        fr4.place(x=0 + 308, y=191)
        fr4.pack_propagate(False)
        l1 = Label(fl1, text='办理日期', bg='cyan4', fg='white', font='msserif 17')

        # l1.pack()
        def getid(event=None):
            fl1 = Frame(b_frame, height=38, width=308, bg='cyan4')
            fl1.place(x=0, y=68)
            l1 = Label(fl1, text='办理日期', bg='cyan4', fg='white', font='msserif 17')
            l1.pack()
            fl1.pack_propagate(False)

            fr1 = Frame(b_frame, height=38, width=1080 - 308, bg='white')
            fr1.place(x=0 + 308, y=68)
            l1 = Label(fl1, text='办理日期', bg='cyan4', fg='white', font='msserif 17')
            # l1.pack()
            fr1.pack_propagate(False)

            fl2 = Frame(b_frame, height=38, width=308, bg='cyan4')
            fl2.place(x=0, y=109)
            fl2.pack_propagate(False)
            l1 = Label(fl2, text='办理时间', bg='cyan4', fg='white', font='msserif 17')
            l1.pack()

            fr2 = Frame(b_frame, height=38, width=1080 - 308, bg='white')
            fr2.place(x=0 + 308, y=109)
            fr2.pack_propagate(False)
            l1 = Label(fl1, text='办理日期', bg='cyan4', fg='white', font='msserif 17')
            # l1.pack()

            fl3 = Frame(b_frame, height=38, width=308, bg='cyan4')
            fl3.place(x=0, y=150)
            fl3.pack_propagate(False)
            l1 = Label(fl3, text='总支付金额', bg='cyan4', fg='white', font='msserif 17')
            l1.pack()

            fr3 = Frame(b_frame, height=38, width=1080 - 308, bg='white')
            fr3.place(x=0 + 308, y=150)
            fr3.pack_propagate(False)
            l1 = Label(fl1, text='办理日期', bg='cyan4', fg='white', font='msserif 17')
            # l1.pack()

            fl4 = Frame(b_frame, height=38, width=308, bg='cyan4')
            fl4.place(x=0, y=191)
            fl4.pack_propagate(False)
            l1 = Label(fl4, text='支付方式', bg='cyan4', fg='white', font='msserif 17')
            l1.pack()

            fr4 = Frame(b_frame, height=38, width=1080 - 308, bg='white')
            fr4.place(x=0 + 308, y=191)
            fr4.pack_propagate(False)
            l1 = Label(fl1, text='办理日期', bg='cyan4', fg='white', font='msserif 17')
            idd = p_id.get()

            # print (idd)
            # cur.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar,totalamt varchar)")
            cur.execute("select * from payments where id = ?", (idd,))
            x = cur.fetchall()
            # print(x)
            cur.execute("select day,month,year,time,totalamt,r_n,method from paymentsf where id = ?", (idd,))
            yy = cur.fetchone()

            # print (x)
            if (yy != None):
                dot = yy[0] + '-' + yy[1] + '-' + yy[2]
                tot = yy[3]
                ap = yy[4]
                pm = yy[6]
                l1 = Label(fr1, text=dot, height=38, width=1080 - 308, font='msserif 15', bg='white', fg='cyan4').pack()
                l2 = Label(fr2, text=tot, height=38, width=1080 - 308, font='msserif 15', bg='white', fg='cyan4').pack()
                l3 = Label(fr3, text=ap, height=38, width=1080 - 308, font='msserif 15', bg='white', fg='cyan4').pack()
                l4 = Label(fr4, text=pm, height=38, width=1080 - 308, font='msserif 15', bg='white', fg='cyan4').pack()
            else:
                l1 = Label(fr1, text='无有效信息', height=38, width=1080 - 308, font='msserif 15', bg='white',
                           fg='cyan4').pack()
                l1 = Label(fr2, text='无有效信息', height=38, width=1080 - 308, font='msserif 15', bg='white',
                           fg='cyan4').pack()
                l1 = Label(fr3, text='无有效信息', height=38, width=1080 - 308, font='msserif 15', bg='white',
                           fg='cyan4').pack()
                l1 = Label(fr4, text='无有效信息', height=38, width=1080 - 308, font='msserif 15', bg='white',
                           fg='cyan4').pack()

        ok = Button(hline, text='√', font='msserif 10', bg='white', activebackground='steelblue', fg='cyan4',
                    command=getid)
        ok.place(x=530, y=5)
        p_id.bind('<Return>', getid)

        def pr():
            messagebox.askyesno("打印", "是否打印收据？")

        pinv = Button(b_frame, text='打印收据', bg='Green', fg='white', command=pr).place(x=976, y=235)
        # ------------内框底框-------------------------

        '''smf1 = Frame(b_frame,height=150,width=175,bg='white')
        tr = Label(smf1,text='Total Rooms:',fg='white',bg='cyan4',width=100,height=2,font='helvetica 15')
        tr.pack(side='top')
        smf1.pack_propagate(False)
        smf1.place(x=0,y=30)
        Label(smf1,fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')

        smf2 = Frame(b_frame,height=150,width=175,bg='white')
        ar = Label(smf2,text='Available Rooms:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
        ar.pack(side='top')
        smf2.pack_propagate(False)
        smf2.place(x=180+4,y=30)
        Label(smf2,fg='cyan4',bg='white',font='msserif 50').place(x=63,y=60)

        smf3 = Frame(b_frame,height=150,width=175,bg='white')
        tre = Label(smf3,text='Total reservations:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
        tre.pack(side='top')
        smf3.pack_propagate(False)
        smf3.place(x=360+6,y=30)
        Label(smf3,fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')

        smf4 = Frame(b_frame,height=150,width=175,bg='white')
        tc = Label(smf4,text='Total Customers:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
        tc.pack(side='top')
        smf4.pack_propagate(False)
        smf4.place(x=540+8,y=30)
        Label(smf4,text='40',fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')

        smf5 = Frame(b_frame,height=150,width=175,bg='white')
        ts = Label(smf5,text='Total Staff:',fg='white',bg='cyan4',width=130,height=2,font='helvetica 15')
        ts.pack(side='top')
        smf5.pack_propagate(False)
        smf5.place(x=720+10,y=30)
        Label(smf5,fg='cyan4',bg='white',font='msserif 50').pack(anchor='center')
        #Label(b_frame,text='==================================================================================',fg='cyan4').place(x=0,y=20)
        #b_frame.pack_propagate(False)
    '''

        nl = Label(b_frame, text='组员：张泽西、臧元祥', fg='black', bg='gray91', font='msserif 8')
        nl.place(x=855, y=310)
        nl.tkraise()

    # ---------------reserve------------------------------------------------------------------------------------------------------------------------

    def reserve():
        b_frame = Frame(root, height=420, width=1080, bg='gray89')
        path = "images/background2.jpg"
        img = ImageTk.PhotoImage(Image.open(path))
        label = Label(b_frame, image=img, height=420, width=1080)
        label.image = img
        label.place(x=0, y=0)

        # hline = Frame(b_frame,height=10,width=960,bg='cyan4')
        # hline.place(x=122,y=27)
        vline = Frame(b_frame, height=400, width=7, bg='lightsteelblue3')
        vline.place(x=700, y=0)

        Label(b_frame, text='个人信息（*为必填项）', font='msserif 15', bg='gray93').place(x=225, y=0)

        fnf = Frame(b_frame, height=1, width=1)
        fn = Entry(fnf)

        mnf = Frame(b_frame, height=1, width=1)
        mn = Entry(mnf)

        lnf = Frame(b_frame, height=1, width=1)
        ln = Entry(lnf)

        fn.insert(0, '姓 *')
        mn.insert(0, '中间名')
        ln.insert(0, '名 *')

        def on_entry_click1(event):
            if fn.get() == '姓 *':
                fn.delete(0, END)
                fn.insert(0, '')

        def on_entry_click2(event):
            if mn.get() == '中间名':
                mn.delete(0, END)
                mn.insert(0, '')

        def on_entry_click3(event):
            if ln.get() == '名 *':
                ln.delete(0, END)
                ln.insert(0, '')

        def on_exit1(event):
            if fn.get() == '':
                fn.insert(0, '姓 *')

        def on_exit2(event):
            if mn.get() == '':
                mn.insert(0, '中间名')

        def on_exit3(event):
            if ln.get() == '':
                ln.insert(0, '名 *')

        fn.bind('<FocusIn>', on_entry_click1)
        mn.bind('<FocusIn>', on_entry_click2)
        ln.bind('<FocusIn>', on_entry_click3)
        fn.bind('<FocusOut>', on_exit1)
        mn.bind('<FocusOut>', on_exit2)
        ln.bind('<FocusOut>', on_exit3)

        fn.pack(ipady=4, ipadx=15)
        mn.pack(ipady=4, ipadx=15)
        ln.pack(ipady=4, ipadx=15)
        fnf.place(x=20, y=42)
        mnf.place(x=235, y=42)
        lnf.place(x=450, y=42)

        Label(b_frame, text='联系方式', font='msserif 15', bg='gray93').place(x=225, y=90)

        cnf = Frame(b_frame, height=1, width=1)
        cn = Entry(cnf)

        emf = Frame(b_frame, height=1, width=1)
        em = Entry(emf)

        adf = Frame(b_frame, height=1, width=1)
        ad = Entry(adf)

        cn.insert(0, '电话号码 *')
        em.insert(0, '邮箱 *')
        ad.insert(0, "住址 *")

        def on_entry_click4(event):
            if cn.get() == '电话号码 *':
                cn.delete(0, END)
                cn.insert(0, '')

        def on_entry_click5(event):
            if em.get() == '邮箱 *':
                em.delete(0, END)
                em.insert(0, '')

        def on_entry_click6(event):
            if ad.get() == "住址 *":
                ad.delete(0, END)
                ad.insert(0, '')

        def on_exit4(event):
            if cn.get() == '':
                cn.insert(0, '电话号码 *')

        def on_exit5(event):
            if em.get() == '':
                em.insert(0, '邮箱 *')

        def on_exit6(event):
            if ad.get() == '':
                ad.insert(0, "住址 *")

        cn.bind('<FocusIn>', on_entry_click4)
        em.bind('<FocusIn>', on_entry_click5)
        ad.bind('<FocusIn>', on_entry_click6)
        cn.bind('<FocusOut>', on_exit4)
        em.bind('<FocusOut>', on_exit5)
        ad.bind('<FocusOut>', on_exit6)

        cn.pack(ipady=4, ipadx=15)
        em.pack(ipady=4, ipadx=15)
        ad.pack(ipady=4, ipadx=15)
        cnf.place(x=20, y=130)
        emf.place(x=235, y=130)
        adf.place(x=450, y=130)
        # l = Label(b_frame,text='Please Enter The Unique Payment ID',font='msserif 15',bg='cyan4',fg='white')
        # l.place(x=245,y=0)

        Label(b_frame, text='预约信息', font='msserif 15', bg='gray93').place(x=210, y=175)

        nocf = Frame(b_frame, height=1, width=1)
        noc = Entry(nocf)

        noaf = Frame(b_frame, height=1, width=1)
        noa = Entry(noaf)

        nodf = Frame(b_frame, height=1, width=1)
        nod = Entry(nodf)

        noc.insert(0, '随行的孩童个数（未成年） *')
        noa.insert(0, '成年人个数 *')
        nod.insert(0, '留宿天数 *')

        def on_entry_click7(event):
            if noc.get() == '随行的孩童个数（未成年） *':
                noc.delete(0, END)
                noc.insert(0, '')

        def on_entry_click8(event):
            if noa.get() == '成年人个数 *':
                noa.delete(0, END)
                noa.insert(0, '')

        def on_entry_click9(event):
            if nod.get() == '留宿天数 *':
                nod.delete(0, END)
                nod.insert(0, '')

        def on_exit7(event):
            if noc.get() == '':
                noc.insert(0, '随行的孩童个数（未成年） *')

        def on_exit8(event):
            if noa.get() == '':
                noa.insert(0, '成年人个数 *')

        def on_exit9(event):
            if nod.get() == '':
                nod.insert(0, '留宿天数 *')

        noc.bind('<FocusIn>', on_entry_click7)
        noa.bind('<FocusIn>', on_entry_click8)
        nod.bind('<FocusIn>', on_entry_click9)
        noc.bind('<FocusOut>', on_exit7)
        noa.bind('<FocusOut>', on_exit8)
        nod.bind('<FocusOut>', on_exit9)

        noc.pack(ipady=4, ipadx=15)
        noa.pack(ipady=4, ipadx=15)
        nod.pack(ipady=4, ipadx=15)
        nocf.place(x=20, y=220)
        noaf.place(x=235, y=220)
        nodf.place(x=450, y=220)

        roomnf = Frame(b_frame, height=1, width=1)
        roomn = Entry(roomnf)
        roomn.insert(0, '输入房间号 *')

        def on_entry_click10(event):
            if roomn.get() == '输入房间号 *':
                roomn.delete(0, END)
                roomn.insert(0, '')

        def on_exit10(event):
            if roomn.get() == '':
                roomn.insert(0, '输入房间号 *')

        roomn.bind('<FocusIn>', on_entry_click10)
        roomn.bind('<FocusOut>', on_exit10)
        roomn.pack(ipady=4, ipadx=15)
        roomnf.place(x=20, y=270)
        var = IntVar()
        pmethod = IntVar()

        def booking():
            if fn.get() == '姓' or ln.get() == '名' or cn.get() == '电话号码 *' or em.get() == '邮箱' or ad.get() == "地址" or noc.get() == '随行的孩童个数（未成年）' or noa.get() == '成年人个数' or nod.get() == '留宿天数' or roomn.get() == '请输入要预定的房间号':
                messagebox.showinfo('Incomplete', '请填写必填项*')
            elif fn.get() == '' or ln.get() == '' or cn.get() == '' or em.get() == '' or ad.get() == "" or noc.get() == '' or noa.get() == '' or nod.get() == '' or roomn.get() == '':
                messagebox.showinfo('Incomplete', '请填写必填项*')
            # cur.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar)")
            else:
                cur.execute("select rstatus from roomd where rn = ?", (roomn.get(),))
                temp = cur.fetchone()
                if temp[0] == 'Reserved':
                    messagebox.showwarning('房间已被预定', 'Room number ' + str(roomn.get()) + ' is Reserved')
                else:
                    payroot = Tk()
                    payroot.title("支付方式")
                    payroot.minsize(height=250, width=252)
                    payroot.configure(bg='White')
                    # global pmethod
                    cur.execute("select price from roomd where rn = (?)", (roomn.get(),))
                    rp = cur.fetchone()
                    
                    var = IntVar()
                    var.set(1)
                    def update_var(new_value):
                        var.set(new_value)
                        pmethod = var.get()
                        print(pmethod)
                    amtpd = str(int(rp[0]) * int(nod.get()))
                    Label(payroot, text='选择支付方式 共计￥' + str(int(rp[0]) * int(nod.get())), font='msserif 14 bold',
                          bg='White').place(x=0, y=10)
                    Frame(payroot, height=4, width=300, bg='cyan4').place(x=0, y=39)
                    Radiobutton(payroot, text='现金  ', bg='White', variable=var, value=1, font='helvetica 15',
                                width=5, command=lambda: update_var(1)).place(x=0, y=50)
                    Radiobutton(payroot, text='银行卡  ', bg='White', variable=var, value=2, font='helvetica 15',
                                width=5, command=lambda: update_var(2)).place(x=10, y=90)
                    Radiobutton(payroot, text='支付宝  ', bg='White', variable=var, value=3, font='helvetica 15',
                                width=5, command=lambda: update_var(3)).place(x=10, y=130)
                    Radiobutton(payroot, text='微信 ', bg='White', variable=var, value=4, font='helvetica 15',
                                width=5, command=lambda: update_var(4)).place(x=0, y=170)


                    
                    

                    def f():
                        pmethod = var.get()
                        paycase = \
                            {
                                1: "现金",
                                2: "银行卡",
                                3: "支付宝",
                                4: "微信"
                            }
                        case = paycase.get(pmethod)
                        if var != '':
                            cur.execute("select id from paymentsf order by id desc")
                            x = cur.fetchone()
                            cid = int(x[0])
                            cid += 1
                            # print (cid)
                            # print (pmethod.get())
                            # cur.execute("create table if not exists paymentsf(id number  primary key,f_name varchar,l_name varchar,c_number varchar,email varchar , r_n number ,day varchar,month varchar,year varchar,time varchar , method varchar,totalamt varchar)")
                            cur.execute("insert into paymentsf values(?,?,?,?,?,?,?,?,?,?,?,?)", (
                            cid, fn.get(), ln.get(), cn.get(), em.get(), roomn.get(), str(now.strftime("%d")),
                            str(now.strftime("%b")), str(now.strftime("%Y")), str(now.strftime("%H:%M")), str(case),
                            amtpd))
                            cur.execute("update roomd set rstatus='Reserved' where rn = ? ", (roomn.get(),))
                            messagebox.showinfo("Successful", "已成功预定房间！")
                            con.commit()
                            ask = messagebox.askyesno("Successful", "已成功付款\n请问您想打印收据吗?")
                            if ask == 'yes':
                                def createfile():
                                    fl = open("reciept.txt", "w")
                                    fl.write("reciept will come here")
                                createfile()
                            reserve()
                            payroot.destroy()
                        else:
                            messagebox.showwarning("Not selected", "请选择支付方式")

                    Button(payroot, text='支付', font='msserif 12', bg='Green', fg='White', width=28, command=f).place(
                        x=0, y=200)
                    Label(payroot, text='您的唯一支付ID是： :', font='msserif', bg='White')  # .place(x=0,y=25)

        def unreserve():

            if (roomn.get() == '请输入要预定的房间号') or (roomn.get() == ''):
                messagebox.showerror('Entries not filled', '请确认输入了房间号')
            else:
                cur.execute("update roomd set rstatus='Unreserved' where rn = ? ", (roomn.get(),))
                messagebox.showinfo("Successful", "已成功取消预定")
                reserve()
                con.commit()

        # --------------------------------------------------------right side---------------------------------------------------
        Label(b_frame, text='筛选', font='msserif 20', bg='gray93').place(x=850, y=0)

        nbb = IntVar()
        acb = IntVar()
        tvb = IntVar()
        wifib = IntVar()

        style = ttk.Style()
        style.map('TCombobox', fieldbackground=[('readonly', 'white')])
        Label(b_frame, text='床数 :', bg='gray93', font='17').place(x=730, y=50)
        # Radiobutton(b_frame,text='1',bg='gray93',variable=nbb,value=1,font='15',width=3).place(x=800,y=50)
        # Radiobutton(b_frame,text='2',bg='gray93',variable=nbb,value=2,font='15',width=3).place(x=880,y=50)
        # Radiobutton(b_frame,text='3',bg='gray93',variable=nbb,value=3,font='15',width=3).place(x=960,y=50)
        nb = ttk.Combobox(b_frame, values=['请选择...', '1', '2', '3'], state='readonly', width=22)
        nb.place(x=830, y=50)
        nb.current(0)

        Label(b_frame, text='网线 :', font='17', bg='gray93').place(x=732, y=75)
        # Radiobutton(b_frame,text='Yes',bg='gray93',variable=acb,value=1,font='15',width=3).place(x=800,y=90)
        # Radiobutton(b_frame,text='No',bg='gray93',variable=acb,value=0,font='15',width=3).place(x=880,y=90)
        ac = ttk.Combobox(b_frame, values=['请选择...', 'Yes', 'No'], state='readonly', width=22)
        ac.place(x=830, y=75)
        ac.current(0)

        Label(b_frame, text='电视 :', font='17', bg='gray93').place(x=732, y=100)
        # Radiobutton(b_frame,text='Yes',bg='gray93',variable=tvb,value=1,font='15',width=3).place(x=800,y=130)
        # Radiobutton(b_frame,text='No',bg='gray93',variable=tvb,value=0,font='15',width=3).place(x=880,y=130)
        tv = ttk.Combobox(b_frame, values=['请选择...', 'Yes', 'No'], state='readonly', width=22)
        tv.place(x=830, y=100)
        tv.current(0)

        Label(b_frame, text='Wifi :', font='17', bg='gray93').place(x=732, y=125)
        # Radiobutton(b_frame,text='Yes',bg='gray93',variable=tvb,value=1,font='15',width=3).place(x=800,y=130)
        # Radiobutton(b_frame,text='No',bg='gray93',variable=tvb,value=0,font='15',width=3).place(x=880,y=130)
        wifi = ttk.Combobox(b_frame, values=['请选择...', 'Yes', 'No'], state='readonly', width=22)
        wifi.place(x=830, y=125)
        wifi.current(0)
        # roomd(rn number primary key,beds number,ac varchar(10),tv varchar(10),internet varchar(10),price number(10))
        listofrooms = Listbox(b_frame, height=6, width=36)
        listofrooms.place(x=735, y=190)
        listofrooms.insert(END, '符合要求的房间将会')
        listofrooms.insert(END, '在填写筛选条件后列出')

        def findrooms():
            cur.execute(
                'select rn,price,rstatus from roomd where beds = ? and ac = ? and tv = ? and internet = ? order by price asc',
                ((nb.get()), ac.get(), tv.get(), wifi.get()))
            x = cur.fetchall()
            # print (x)
            listofrooms.delete(0, END)
            if x == []:
                listofrooms.insert(END, '未找到符合要求的房间')
            for i in x:
                listofrooms.insert(END, '房间号： ' + str(i[0]) + ' - 价格（￥/晚）：' + str(i[1]))

        Res = Button(b_frame, text='预定', bg='white', fg='cyan4', font='timenewroman 11', activebackground='green',
                     command=booking).place(x=235, y=270)
        unres = Button(b_frame, text='取消预定', bg='white', fg='cyan4', font='timenewroman 11',
                       activebackground='green', command=unreserve).place(x=327, y=270)
        findrooms = Button(b_frame, text='查找房间', bg='white', fg='cyan4', font='timenewroman 9',
                           activebackground='green', command=findrooms).place(x=830, y=155)

        scrollbar = Scrollbar(b_frame, orient="vertical")
        scrollbar.config(command=listofrooms.yview)
        scrollbar.place(x=1014, y=191, height=111)
        listofrooms.config(yscrollcommand=scrollbar.set)

        b_frame.place(x=0, y=120 + 6 + 20 + 60 + 11)
        b_frame.pack_propagate(False)
        b_frame.tkraise()

        nl = Label(b_frame, text='组员：张泽西、臧元祥', fg='black', bg='gray91', font='msserif 8')
        nl.place(x=855, y=310)
        nl.tkraise()

    # -------------登出----------------------------------------------------------------------------------------------------------------------
    def login():
        q = messagebox.askyesno("Exit", "您确定要退出吗?")
        if (q):
            root.destroy()

    # ---------------顶框2-----------------------------------------------------------------------------------------------------------------

    sl_frame = Frame(root, height=130, width=1080, bg='white')
    sl_frame.place(x=0, y=70 + 6)
    path = "images/rooms.png"
    img = ImageTk.PhotoImage(Image.open(path))
    b1 = Button(sl_frame, image=img, text='b1', bg='white', width=180, command=rooms)
    b1.image = img
    b1.place(x=180, y=0)
    path2 = "images/hotelstatus.png"
    img1 = ImageTk.PhotoImage(Image.open(path2))
    b2 = Button(sl_frame, image=img1, text='b2', bg='white', width=180, command=hotel_status)
    b2.image = img1
    b2.place(x=0, y=0)
    path3 = 'images/guests.png'
    img3 = ImageTk.PhotoImage(Image.open(path3))
    b3 = Button(sl_frame, image=img3, text='b2', bg='white', width=180, command=staff)
    b3.image = img3
    b3.place(x=180 * 4, y=0)
    path4 = 'images/payments.png'
    img4 = ImageTk.PhotoImage(Image.open(path4))
    b4 = Button(sl_frame, image=img4, text='b2', bg='white', width=180, command=payments)
    b4.image = img4
    b4.place(x=180 * 3, y=0)
    path5 = 'images/logout.png'
    img5 = ImageTk.PhotoImage(Image.open(path5))
    b5 = Button(sl_frame, image=img5, text='b2', bg='white', width=180, height=100, command=login)
    b5.image = img5
    b5.place(x=180 * 5, y=0)
    path6 = 'images/Bookroom.png'
    img6 = ImageTk.PhotoImage(Image.open(path6))
    b6 = Button(sl_frame, image=img6, text='b2', bg='white', width=180, height=100, command=reserve)
    b6.image = img6
    b6.place(x=180 * 2, y=0)
    Label(sl_frame, text='酒店明细', font='msserif 13', bg='white').place(x=50, y=106)
    Label(sl_frame, text='房间', font='msserif 13', bg='white').place(x=248, y=106)
    Label(sl_frame, text='预定', font='msserif 13', bg='white').place(x=432, y=106)
    Label(sl_frame, text='联系我们', font='msserif 13', bg='white').place(x=774, y=106)
    Label(sl_frame, text='交易查询', font='msserif 13', bg='white').place(x=600, y=106)
    Label(sl_frame, text='退出', font='msserif 13', bg='white').place(x=968, y=106)
    sl_frame.pack_propagate(False)
    # -------------------extra frame------------------------------------------------------------------------------------------------------------------
    redf = Frame(root, height=6, width=1080, bg='lightsteelblue3')
    redf.place(x=0, y=70)
    redf1 = Frame(root, height=40, width=1080, bg='lightsteelblue3')
    redf1.place(x=0, y=210)
    # -------------------------------------------------------------------------------------------------------------------------------------------------
    # hotel_status() # calling the bottom frame for default page
    # login()
    # rooms()
    # payments()
    # cur.execute("select * from roomd ")
    # x = cur.fetchall()
    # print (x)
    reserve()
    # staff()
    datetime()
    mainloop()

def main():
    login = login_system.Login()
    login.root.mainloop()
    # 如果登录成功，执行 mainroot 函数
    if login.login_success == 1:
        start()
        mainroot()
    else:
        sys.exit()