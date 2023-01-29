import sqlite3
import pandas as pd
import util as myutil
import json as json
import student_dao as student
#author:brini581
#Date:2023-01-29
#Desc:Insert student's balance

def SaveStudentMoney(data):

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    count=student.countStudent(data['liuId'])
    if count>0:

        countmoney=countBalance(data['liuId'])
        print("#### ",countmoney)
        if countmoney==0:

            q1 = "CREATE TABLE IF NOT EXISTS money (liuId TEXT PRIMARY KEY,amount INTEGER,currency TEXT,regdate TEXT)"
            cursor.execute(q1)
            q2 = "INSERT INTO money VALUES(?,?,?,?)"
            cursor.execute(q2,(data['liuId'],data['amount'],data['currency'],myutil.getCurrentDate()))
            conn.commit()
            conn.close()
            res={"message":"Successfully Inserted"}
        else:
            q3 = "UPDATE money SET amount=?,currency=?,regdate=? WHERE liuId=?"
            cursor.execute(q3,((data['amount'],data['currency'],myutil.getCurrentDate(),data['liuId'])))
            conn.commit()
            conn.close()
            res={"message":"Successfully Updated"}
    else:
        res={"message":"The User neeed to be registered First"}

    return res



def getStudentBalance(data):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    q1 = "SELECT * FROM money WHERE liuId=?"
    result = cursor.execute(q1,(data['liuId'],))
    row = result.fetchone()



    if row:
        # Get the column names
        columns = [col[0] for col in cursor.description]
       # Create a dictionary from the row and column names
        data = dict(zip(columns, row))
        # Convert the dictionary to a JSON object
        json_data = json.dumps(data)
        user=json_data
    else:
        user={"message":"No Balance"}

    return user
    

def countBalance(liu):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    q1 = "SELECT COUNT(*) FROM money WHERE liuId=?"
    result = cursor.execute(q1,(liu,))
    count = result.fetchone()[0]
    if count>0:
        res =count
    else:
        res = 0

    return res
