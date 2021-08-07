import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector
import easygui

try:
    # add your databse details.
    mydb = mysql.connector.connect(
        host="db4free.net",
        user="codebot",
        password="1601Mybday",
        database="codebot"
    )
    cur = mydb.cursor()
    create_table = "CREATE TABLE if not exists account_table(name varchar(20),roll int(3),pass varchar(20))"
    cur.execute(create_table)
    query = "CREATE table if not exists subjects(ro int(5),subject varchar(20),ca int(4),tc int(4))"
    cur.execute(query)
except:    
    easygui.msgbox("No Internet")


def main_window():
    root = tk.Tk()
    root.title("Attendance manager")
    canvas = tk.Canvas(root, width=900, height=550, )
    canvas.pack()
    frame_1 = tk.Frame(root, bg="#2C2B2B")
    frame_1.place(relx=0.345, rely=0.04, relheight=0.1, relwidth=0.3)
    label_title = tk.Label(frame_1, text="Attendance Manager", fg='black')
    label_title.place(relx=0.028, rely=0.24)
    label_title.config(font=("stencil", 14))
    login_button = tk.Button(root, text="Login", bg="black", fg="red", bd=5, font='50', command=lambda: login_tk())
    login_button.place(relx=0.43, rely=0.3, relwidth=0.15, relheight=0.1)
    logup_button = tk.Button(root, text="signup", bg="black", fg="red", bd=5, font='50', command=lambda: sign_up_tk())
    logup_button.place(relx=0.43, rely=0.45, relwidth=0.15, relheight=0.1)
    root.mainloop()


def sign_up_tk():
    root = tk.Tk()
    root.title("Attendance manager")
    canvas = tk.Canvas(root, width=900, height=550, bg="black")
    canvas.pack()
    frame_1 = tk.Frame(root, bg="#2C2B2B")
    frame_1.place(relx=0.345, rely=0.04, relheight=0.1, relwidth=0.3)
    label_title = tk.Label(frame_1, text="Attendance Manager", fg='black')
    label_title.place(relx=0.028, rely=0.24)
    label_title.config(font=("stencil", 14))
    e1 = tk.Entry(root, text="name", bg="white", fg="black", bd=5)
    e1.place(relx=0.37, rely=0.25, relheight=0.07, relwidth=0.25)
    e2 = tk.Entry(root, text="roll no.", bg="white", fg="black", bd=5)
    e2.place(relx=0.37, rely=0.35, relheight=0.07, relwidth=0.25)
    e3 = tk.Entry(root, text="password", bg="white", fg="black", bd=5)
    e3.place(relx=0.37, rely=0.45, relheight=0.07, relwidth=0.25)
    signup_button = tk.Button(root, text="signup", bg="black", fg="red", bd=5, font='50',
                              command=lambda: sign_up(e1.get(), e2.get(), e3.get()))
    signup_button.place(relx=0.37, rely=0.55, relwidth=0.15, relheight=0.1)

    root.mainloop()


def login_tk():
    root = tk.Tk()
    root.title("Attendance manager")
    canvas = tk.Canvas(root, width=900, height=550, bg="black")
    canvas.pack()
    frame_1 = tk.Frame(root, bg="#2C2B2B")
    frame_1.place(relx=0.345, rely=0.04, relheight=0.1, relwidth=0.3)
    label_title = tk.Label(frame_1, text="Attendance Manager", fg='black')
    label_title.place(relx=0.028, rely=0.24)
    label_title.config(font=("stencil", 14))
    e1 = tk.Entry(root, text="name", bg="white", fg="black", bd=5)
    e1.place(relx=0.37, rely=0.25, relheight=0.07, relwidth=0.25)
    e2 = tk.Entry(root, text="roll no.", bg="white", fg="black", bd=5)
    e2.place(relx=0.37, rely=0.35, relheight=0.07, relwidth=0.25)
    login_button = tk.Button(root, text="Login", bg="black", fg="red", bd=5, font='50',
                             command=lambda: login(e1.get(), e2.get()))
    login_button.place(relx=0.37, rely=0.45, relwidth=0.15, relheight=0.1)

    root.mainloop()


def login_tk_page(nm, rn):
    root = tk.Tk()
    root.title("Attendance manager")
    canvas = tk.Canvas(root, width=900, height=550, bg="black")
    canvas.pack()
    frame_1 = tk.Frame(root, bg="#2C2B2B")
    frame_1.place(relx=0.345, rely=0.04, relheight=0.1, relwidth=0.3)
    label_title = tk.Label(frame_1, text="Attendance Manager", fg='black')
    label_title.place(relx=0.028, rely=0.24)
    label_title.config(font=("stencil", 14))
    label_entry = tk.Label(root, text="welcome : {}".format(nm), fg="black")
    label_entry.place(relx=0.028, rely=0.14)
    label_entry.config(font=("stencil", 8))
    es = tk.Entry(root, bg="white", fg="black", bd=5)
    es.place(relx=0.1, rely=0.25, relheight=0.07, relwidth=0.25)
    es1 = tk.Entry(root, bg="white", fg="black", bd=5)
    es1.place(relx=0.1, rely=0.4, relheight=0.07, relwidth=0.25)
    plus_button = tk.Button(root, text="+", bg="black", fg="red", bd=5, font='50',
                            command=lambda: add_class(rn, es.get()))
    plus_button.place(relx=0.4, rely=0.25, relwidth=0.08, relheight=0.08, )
    sub_button = tk.Button(root, text="-", bg="black", fg="red", bd=5, font='50',
                           command=lambda: sub_class(rn, es.get()))
    sub_button.place(relx=0.5, rely=0.25, relwidth=0.08, relheight=0.08)
    per_button = tk.Button(root, text="%", bg="black", fg="red", bd=5, font='50',
                           command=lambda: sub_percentage(rn, es.get()))
    per_button.place(relx=0.6, rely=0.25, relwidth=0.08, relheight=0.08)
    add_sub_button = tk.Button(root, text="Add Subject", bg="black", fg="red", bd=5, font='50',
                               command=lambda: add_subject(rn, es1.get()))
    add_sub_button.place(relx=0.4, rely=0.4, relwidth=0.15, relheight=0.08)
    tper_button = tk.Button(root, text="total %", bg="black", fg="red", bd=5, font='50',
                            command=lambda: total_percentage(rn))
    tper_button.place(relx=0.4, rely=0.65, relwidth=0.15, relheight=0.08)
    root.mainloop()


def sign_up(e1, e2, e3):
    if e1 != "" and e2 != "" and e3 != "":
        insert_table = "INSERT into account_table(name,roll,pass) values(%s,%s,%s)"
        values = (e1.upper(), e2, e3)
        cur.execute(insert_table, values)
        mydb.commit()
        easygui.msgbox("Account Created!", title="Sign_up")
    else:
        easygui.msgbox("Fill full form", title="attention!")


def login(e1, e2):
    try:
        fetch_query = "SELECT * from account_table where roll = %s"
        cur.execute(fetch_query, (e1,))
        result = cur.fetchall()
        [(n, r, p)] = result
        if str(e2) == str(p):
            login_tk_page(n, r)
        else:
            easygui.msgbox("Wrong Password", title="error")
    except:
        easygui.msgbox("Fields empty/no account present")


def add_subject(rln, e):
    if e != "":
        query_1 = "INSERT into subjects(ro,subject,ca,tc) values(%s,%s,%s,%s)"
        values = (rln, e.upper(), 0, 0)
        cur.execute(query_1, values)
        mydb.commit()
        easygui.msgbox("subject added!")
    else:
        easygui.msgbox("Fill full form", title="attention!")


def add_class(rln, e):
    if e != "":
        query = "UPDATE subjects set ca = ca + 1  where ro = %s and subject = %s"
        query1 = "UPDATE subjects set tc = tc + 1  where ro = %s and subject = %s"
        values = (rln, e.upper())
        cur.execute(query, values)
        cur.execute(query1, values)
        mydb.commit()
        easygui.msgbox("class attended")
    else:
        easygui.msgbox("Fill full form", title="attention!")


def sub_class(rln, e):
    if e != "":
        query = "UPDATE subjects set tc = tc + 1 where ro = %s and subject = %s"
        values = (rln, e)
        cur.execute(query, values)
        mydb.commit()
        easygui.msgbox("class missed")
    else:
        easygui.msgbox("Fill full form", title="attention!")


def sub_percentage(rln, e):
    if e != "":
        query = "select * from subjects where ro = %s and subject = %s"
        values = (rln, e)
        cur.execute(query, values)
        result = cur.fetchall()
        [(roln, sub, c, t)] = result
        percent = (int(c) / int(t)) * 100
        easygui.msgbox("Attendance is {}%".format(percent), title="{} Attendance".format(sub))
    else:
        easygui.msgbox("Fill full form", title="attention!")


def total_percentage(rln):
    query_ca = "select sum(ca) from subjects where ro = %s"
    query_tc = "select sum(tc) from subjects where ro = %s"
    cur.execute(query_ca, (rln,))
    result_ca = cur.fetchall()
    [(cat,)] = result_ca
    cur.execute(query_tc, (rln,))
    result_tc = cur.fetchall()
    [(tct,)] = result_tc
    percentage = int((int(cat) / int(tct)) * 100)
    easygui.msgbox("your total Attendance is {}%".format(percentage), title="total Attendance")


main_window()