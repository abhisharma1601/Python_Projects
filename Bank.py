import random
import sqlite3

mydb = sqlite3.connect('bank.db')
cur = mydb.cursor()
acc_table = "CREATE TABLE if not exists acc_table(Name varchar(40),YourName varchar(40),AcNo int(10),Bal int(20))"
cur.execute(acc_table)


def create_acc():
    print("enter Bank Name: ")
    N = input()
    print("enter your name: ")
    YN = input()
    AN = random.randint(111111, 222222)
    print("enter balance:")
    B = input()
    acc_data = 'insert into acc_table(Name,YourName,AcNo,Bal) values(?,?,?,?)'
    data = (N.upper(), YN.upper(), AN, B)
    cur.execute(acc_data, data)
    mydb.commit()
    print("Account created with Acc. Number:\n{}".format(AN))


def transaction():
    for i in range(0, 100):
        print("press A to add money\nPress W to withdraw money\nPress Q to quit")
        y = input()
        if y.lower() == "a":
            print("enter acc. no?")
            A = input()
            print("enter money")
            M = input()
            ad = "UPDATE acc_table Set Bal =Bal + ? where AcNo=?"
            values = (M, A)
            cur.execute(ad, values)
            mydb.commit()
            data_abs = "select * from acc_table where AcNo = ? "
            cur.execute(data_abs, (A,))
            result = cur.fetchall()
            [(name, yn, acn, bal)] = result
            print("New Balance updated\n{}Rs".format(bal))

        elif y.lower() == 'w':
            print("enter acc. no?")
            A = input()
            print("Enter money you want to withdraw:")
            W = input()
            data_abs = "select * from acc_table where AcNo = ?"
            cur.execute(data_abs, (A,))
            result1 = cur.fetchall()
            [(name, yn, acn, bal)] = result1
            if int(W) <= int(bal):
                ad = "UPDATE acc_table Set Bal =Bal - ? where AcNo=?"
                values = (W, A)
                cur.execute(ad, values)
                mydb.commit()
                data_abs = "select * from acc_table where AcNo = ?"
                cur.execute(data_abs, (A,))
                result1 = cur.fetchall()
                [(name, yn, acn, bal)] = result1
                print("New Balance updated\n{}".format(bal))
            else:
                print("entering invalid amount")
                continue
        else:
            print("thanks for visiting. Visit again")
            break


def delete_acc():
    A = input("Enter Account number to be deleted:\n")
    dacc = "delete from acc_table where AcNo = ?"
    cur.execute(dacc, (A,))
    mydb.commit()
    print("Account deleted successfully!")


def check_balance():
    A = input("Enter Account number:\n")
    bal = "select * from acc_table where AcNo = ?"
    cur.execute(bal, (A,))
    result = cur.fetchall()
    [(n, yn, ac, b)] = result
    print("your balance is :\n{}Rs".format(b))


def acc_info():
    A = input("Enter Account number:\n")
    bal = "select * from acc_table where AcNo = ?"
    cur.execute(bal, (A,))
    result = cur.fetchall()
    [(n, yn, ac, b)] = result
    print("your bank is :\n{}\nyour Acc No.:\n{}\nYour balance:\n{}Rs".format(n, ac, b))


print("\t\t\t\t\t\tWELCOME TO ALL IN ONE BANK")
for _ in range(100):
    print("press accordingly:")
    print(
        "1. add account\t\t\t\t2. delete account\t\t\t\t3. Transaction\n4.check Balance\t\t\t\t5. Account Info\t\t\t\t\t6. to quit")
    I = input()
    if I == "1":
        create_acc()
        continue
    elif I == "3":
        transaction()
        continue
    elif I == "2":
        delete_acc()
        continue
    elif I == "4":
        check_balance()
        continue
    elif I == "5":
        acc_info()
        continue
    elif I.lower() == "6":
        break