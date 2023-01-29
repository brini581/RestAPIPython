import sqlite3
import pandas as pd
import util as myutil
#author:brini581
#Date:2023-01-29
#Desc:Insert student details

def registerStudent(data):

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    
    q1 = "CREATE TABLE IF NOT EXISTS user (liuId TEXT PRIMARY KEY,fistName TEXT,lastName TEXT,deptment TEXT,regdate TEXT)"
    cursor.execute(q1)
    q2 = "INSERT INTO user VALUES(?,?,?,?,?)"
    
    cursor.execute(q2,(data['liuId'],data['fistName'],data['lastName'],data['deptment'],myutil.getCurrentDate()))
    conn.commit()
    conn.close()
    return {"message":"Successfully Registered"}



def getStudent(data):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    q1 = "SELECT * FROM user WHERE liuId=?"
    result = cursor.execute(q1,(data['liuId'],))
    row = result.fetchone()


    if row:
        df = pd.read_sql(f"SELECT * FROM user WHERE liuId='{data['liuId']}'",conn)
        json_data = df.to_json()
        df1 = pd.read_json(json_data)
        # Extract the values we need
        liuId = df1.liuId[0]
        firstName = df1.fistName[0]
        lastName = df1.lastName[0]
        deptment = df1.deptment[0]
        user ={"liuId":liuId,"firstName":firstName,"lastName":lastName,"deptment":deptment}
    else:
        user = {"message":"User Not Registered"}

    return user

def countStudent(liu):
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    q1 = "SELECT COUNT(*) FROM user WHERE liuId=?"
    result = cursor.execute(q1,(liu,))
    count = result.fetchone()[0]
    if count>0:
        res =count
    else:
        res = 0

    return res