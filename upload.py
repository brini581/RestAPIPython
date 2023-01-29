from flask import  jsonify, request
from flask import Blueprint
import util as myutil
import upload_dao  as db
upload_routes = Blueprint("upload_routes", __name__)
#author:brini581
#Date:2023-01-29
#Desc:upload

@upload_routes.route('/uploadFile', methods=['POST'])
def uploadFile():

    liuId = request.headers.get("liuId")
    if "file" not in request.files:
        return "No file found"
    file = request.files["file"]
    file_info=myutil.uploadFile(file,liuId)
    
    message=db.uploadFile(file_info,liuId)


    return jsonify(message)