import mysql.connector


def get_data():
    mydb = mysql.connector.connect(host = "localhost",user="root", password="root", database="testdb")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT*FROM employee")
    result = mycursor.fetchmany()
    mycursor.close()
    return result