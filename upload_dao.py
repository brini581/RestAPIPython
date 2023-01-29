import sqlite3
import util as myutil
import student_dao as student

#author:brini581
#Date:2023-01-29
#Desc:Insert upload details

def uploadFile(data,liuId):

    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    
    count=student.countStudent(liuId)
    if count>0:
        q1 = "CREATE TABLE IF NOT EXISTS fileinfo (liuId TEXT ,fileName TEXT,filePath TEXT,fileFormat TEXT ,filePages INTEGER,pagePrice INTEGER,totalPrice INTEGER, regdate TEXT,PRIMARY KEY (liuId,fileName))"
        cursor.execute(q1)
        q2 = "INSERT INTO fileinfo VALUES(?,?,?,?,?,?,?,?)"
        cursor.execute(q2,(liuId,data[0],data[1],data[2],data[3],100,100*data[3],myutil.getCurrentDate()))
        conn.commit()
        conn.close()
        res={"message":"Successfully uploaded and inserted"}
    else:
        res={"message":"The user needed to be registered first"}

    return res