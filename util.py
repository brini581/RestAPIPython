from flask import request
import os 
from datetime import datetime
import PyPDF2
#author:brini581
#Date:2023-01-29
#Desc:Util
def getCurrentDate():
     today = datetime.now().strftime('%Y%m%d%H%M%S')
     return today

#Uploading the file to specified folder
def uploadFile(file,liuId):
    today = datetime.now().strftime('%Y%m%d')
    main_dir = f"/Practice/{liuId}/{today}/"
    isExist = os.path.exists(main_dir)
    if(isExist==False):
        os.makedirs(main_dir)
    filename=f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{file.filename}"
    file.save(os.path.join(main_dir,filename))
    
    #Counting doc pages
    pdf =PyPDF2.PdfReader(file)
    numberPages=len(pdf.pages)

    fileFormat=file.content_type
    file_inof=[filename,main_dir,fileFormat,numberPages]
    return file_inof