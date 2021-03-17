# !/usr/bin/python3

import subprocess as sp
import pymysql
import pymysql.cursors
from prettytable import PrettyTable



def insertgood():
    global cur
    try:
        row = {}
        print("Enter new good details: ")
        row["GOOD_ID"] = int(input("GOOD ID: "))
        row["GOOD_TYPE"] = input("GOOD TYPE: ")
        row["BRAND"] = input("BRAND: ")
        row["MRP"] = int(input("MRP: "))
        row["MANUFACTURE_DATE"] = input("MANUFACTURE DATE: ")
        row["EXPIRY_DATE"] = input("EXPIRY DATE: ")
        row["NET_WEIGHT"] = int(input("NET WEIGHT:  "))
        row["TRADE_MARK"] = (input("TRADE MARK:  "))
    
        query = "INSERT INTO GOODS(GOOD_ID,GOOD_TYPE,BRAND,MRP,MANUFACTURE_DATE,EXPIRY_DATE,NET_WEIGHT,TRADE_MARK) VALUES('%d', '%s', '%s', %d, '%s', '%s', '%d', '%s')" %(row["GOOD_ID"], row["GOOD_TYPE"], row["BRAND"], row["MRP"], row["MANUFACTURE_DATE"], row["EXPIRY_DATE"], row["NET_WEIGHT"], row["TRADE_MARK"])

        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
    return


def insertemployee():
    global cur
    try:
        row = {}
        print("Enter new employee's details: ")
        row["EMPLOYEE_ID"] = int(input("EMPLOYEE_ID: "))
        name = (input("Name (Firstname Lastname): ")).split(' ')
        row["FIRST_NAME"] = name[0]
        row["LAST_NAME"] = name[1]

        row["MOTHER'S_NAME"] = input("MOTHER'S NAME: ")
        row["FATHER'S_NAME"] = input("FATHER'S NAME: ")
        row["QUALIFICATION"] = input("QUALIFICATION: ")
        row["DOB"] = input("DOB: ")
        row["DATE_OF_RECRUITMENT"] = input("DATE OF RECRUITMENT : ")
        row["MOBILE_NUMBER"] = input("MOBILE NUMBER: ")
        row["EMPLOYEE_TYPE"] = input("EMPLOYEE TYPE: ")
        row["SALARY"] = int(input("SALARY: "))
        row["BRANCH_ID"] = int(input("BRANCH_ID: "))

        query= "INSERT INTO EMPLOYEE(EMPLOYEE_ID,FIRST_NAME,LAST_NAME,`MOTHER'S_NAME`,`FATHER'S_NAME`,QUALIFICATION,DOB,DATE_OF_RECRUITMENT,MOBILE_NUMBER,EMPLOYEE_TYPE,SALARY,BRANCH_ID) VALUES(%d,'%s','%s','%s','%s','%s','%s','%s','%s','%s', %d, %d)" %(row["EMPLOYEE_ID"],row["FIRST_NAME"],row["LAST_NAME"],row["MOTHER'S_NAME"],row["FATHER'S_NAME"],row["QUALIFICATION"],row["DOB"],row["DATE_OF_RECRUITMENT"],row["MOBILE_NUMBER"],row["EMPLOYEE_TYPE"],row["SALARY"],row["BRANCH_ID"])
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
    return


def insertbranch():
    try:
        global cur
        row = {}
        print("Enter new branch details: ")
        row["BRANCH_ID"] = int(input("BRANCH_ID: "))
        row["LOCATION.STREETNAME"] = input("LOCATION.STREETNAME: ")
        row["LOCATION.CITY"] = input("LOCATION.CITY: ")
        row["LOCATION.DISTRICT"] = input("LOCATION.DISTRICT: ")
        row["LOCATION.STATE"] = input("LOCATION.STATE: ")
        row["PARTNER_ID"] =int(input("PARTNER_ID: "))

        query = "INSERT INTO BRANCH(BRANCH_ID, `LOCATION.STREETNAME`, `LOCATION.CITY`, `LOCATION.DISTRICT`, `LOCATION.STATE`, PARTNER_ID) VALUES('%d', '%s', '%s', '%s', '%s', '%d')" %(row["BRANCH_ID"], row["LOCATION.STREETNAME"], row["LOCATION.CITY"], row["LOCATION.DISTRICT"], row["LOCATION.STATE"], row["PARTNER_ID"])
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
    return

def insertsupplier():
    try:
        global cur
        row = {}
        print("Enter new supplier details: ")
        row["SUPPLIER_ID"] = int(input("SUPPLIER_ID: "))
        row["NAME"] = input("NAME: ")
        query = "INSERT INTO SUPPLIER(SUPPLIER_ID,NAME) VALUES(%d, '%s')" %(row["SUPPLIER_ID"],row["NAME"])
        cur.execute(query)
        con.commit()
        print("Inserted Into Database")
    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e)
    return
optionFunctionMapping = {
    1: insertgood,
    2: insertemployee,
    3: insertbranch,
    4: insertsupplier,
}

def listemployee(con):
    print("Employee data:")
    cursor = con.cursor()
    sql = "SELECT * FROM EMPLOYEE"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        result = cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["EMPLOYEE_ID", "FIRST_NAME", "LAST_NAME", "DATE_OF_RECRUITMENT", "EMPLOYEE_TYPE", "SALARY"]
        for row in result:
            # print(row)
            # print(row['NAME'],row['VIP'],row['COST'])
            new_row = [row["EMPLOYEE_ID"], row["FIRST_NAME"], row["LAST_NAME"], row["DATE_OF_RECRUITMENT"], row["EMPLOYEE_TYPE"], row["SALARY"]]
            table.add_row(new_row)
        print(table)
        # Commit your changes in the database
        con.commit()
    except:
        # Rollback in case there is any error
        con.rollback()

def listgood(con):
    print("Good data:")
    cursor = con.cursor()
    sql = "SELECT GOOD_ID,count(*) FROM SUPPLY GROUP BY GOOD_ID"
    try:
        # Execute the SQL command
        cursor.execute(sql)
        result = cursor.fetchall()
        table = PrettyTable()
        table.field_names = ["GOOD_ID", "NUMBER OF BRANCHES IN WHICH IT IS SOLD"]
        for row in result:
            new_row = [row["GOOD_ID"], row["count(*)"]]
            table.add_row(new_row)
        print(table)
        # Commit your changes in the database
        con.commit()
    except:
        # Rollback in case there is any error
        con.rollback()

def updateemployeesalary():
    while True:
        try:
            cid=int(input("Enter the Id of the employee whose salary is to be updated: "))
            new_salary=int(input("Enter the New salary: "))
        except ValueError:
            print("Please Enter a valid integer")
            continue
        else:
            break
    query="UPDATE EMPLOYEE SET SALARY = %d WHERE EMPLOYEE_ID = %d" % (new_salary, cid) 
    try:
        cur.execute(query)
        con.commit()
        print("Salary Updated")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e) 
    return

def deletegood():
    delid=int(input("Enter the Id of the Good to be deleted: "))
    query="DELETE FROM GOODS WHERE GOOD_ID=%d" %(delid) 
    try:
        cur.execute(query)
        con.commit()
        print("Good Deleted")

    except Exception as e:
        print("in exception")
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e) 

    return

def deleteemp():
    delid=int(input("Enter the Id of the Employee to be deleted: "))
    query="DELETE FROM EMPLOYEE WHERE EMPLOYEE_ID=%d" %(delid) 
    try:
        cur.execute(query)
        con.commit()
        print("Employee Deleted")

    except Exception as e:
        print("in exception")
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e) 

    return

def deletebranch():
    delid=int(input("Enter the Id of the Branch to be deleted: "))
    query="DELETE FROM BRANCH WHERE BRANCH_ID=%d" %(delid) 
    try:
        cur.execute(query)
        con.commit()
        print("Branch Deleted")

    except Exception as e:
        print("in exception")
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e) 

    return

def deletesupp():
    delid=int(input("Enter the Id of the Supplier to be deleted: "))
    query="DELETE FROM SUPPLIER WHERE SUPPLIER_ID=%d" %(delid) 
    try:
        cur.execute(query)
        con.commit()
        print("Supplier Deleted")

    except Exception as e:
        print("in exception")
        con.rollback()
        print("Failed to insert into database")
        print (">>>>>>>>>>>>>", e) 

    return
        
while(1):
    tmp = sp.call('clear',shell=True)
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(host='localhost',
                user=username,
                password=password,
                db='SUPERMARKET',
                cursorclass=pymysql.cursors.DictCursor)
        with con:
            cur = con.cursor()
            while(1):
                tmp = sp.call('clear',shell=True)
                print("1. Insert a new Good")
                print("2. Insert a new Employee")
                print("3. Insert a new Branch")
                print("4. Insert a new Supplier")
                print("5. View the list of all the Employees")
                print("6. View the list of all the sold Goods")
                print("7. Update Employee Salary")
                print("8. Delete a Good entry when it is sold in all branches")
                print("9. Delete an Employee entry when he/she stops working")
                print("10. Delete a Branch entry when it is removed")
                print("11. Delete a Supplier entry when he/she stops supplying")
                c = int(input("Enter choice --> "))
                tmp = sp.call('clear',shell=True)
                if c==1:
                    insertgood()
                elif c==2:
                    insertemployee()
                elif c==3:
                    insertbranch()
                elif c==4:
                    insertsupplier()
                elif c==5:
                    listemployee(con)
                elif c==6:
                    listgood(con)
                elif c==7:
                    updateemployeesalary()
                elif c==8:
                    deletegood()
                elif c==9:
                    deleteemp()
                elif c==10:
                    deletebranch()
                elif c==11:
                    deletesupp()



    except Exception as e:
        tmp = sp.call('clear',shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        print("ERROR: ",e)
        tmp = input("Enter any key to CONTINUE>")