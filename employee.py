from flask import Flask, render_template, request
import sqlite3 as sql

connection = sql.connect("employeedata.db", check_same_thread=False)
listofemployee = connection.execute("select * from sqlite_master where type='table' AND name='employee'").fetchall()

if listofemployee != []:
    print("Table exist already")
else:
    connection.execute('''create table employee(
                                ID integer primary key autoincrement,
                                Empcode text,
                                Empname text,
                                age integer,
                                address text,
                                email text,
                                designation text,
                                salary integer                            
                                companyname text                             
                                );''')
    print("Table Created Successfully")

employee = Flask(__name__)


@employee.route("/add", methods=["GET", "POST"])
def Employee_details():
    if request.method == "POST":
        getEmpcode = request.form["empcode"]
        getEmpname = request.form["empname"]
        getage = request.form["age"]
        getaddress = request.form["address"]
        getemail = request.form["email"]
        getdesignation = request.form["designation"]
        getsalary = request.form["salary"]
        getcompanyname = request.form["companyname"]
        print(getEmpcode)
        print(getEmpname)
        print(getage)
        print(getaddress)
        print(getemail)
        print(getdesignation)
        print(getsalary)
        print(getcompanyname)

        try:
            query = "insert into employee(Empcode,Empname,age,address,email,designation,salary) values('" + getEmpcode + "','" + getEmpname + "'," + getage + ",'" + getaddress + "','" + getemail + "','" + getdesignation + "'," + getsalary + ")"
            print(query)
            connection.execute(query)
            connection.commit()
            connection.close()
            print("Employee Data Added Successfully.")
        except Exception as err:
            print("Error occured ", err)

    return render_template("add.html")


@employee.route("/search")
def Search():
    return render_template("search.html")


@employee.route("/update")
def Update():
    return render_template("update.html")


@employee.route("/delete")
def Delete():
    return render_template("delete.html")


@employee.route("/viewall")
def viewAll():
    cursor = connection.cursor()
    count = cursor.execute("select * from employee")
    result = cursor.fetchall()
    return render_template("viewall.html", employee=result)


if __name__ == "__main__":
    employee.run()
