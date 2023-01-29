import os 
from datetime import date
today = date.today().strftime('%Y%m%d')
main_dir = f"/Practice/{today}"
isExist = os.path.exists(main_dir)
if(isExist==False):
    os.makedirs(main_dir)


 