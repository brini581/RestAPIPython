from flask import  jsonify, request
import util as myutil
from flask import Blueprint
import student_dao  as db
#author:brini581
#Date:2023-01-29
#Desc:register student endpoint

register_routes = Blueprint("register_routes", __name__)
@register_routes.route('/')
def home():
    return "LiU Paper Cut Is UP and Running"


@register_routes.route('/registerStudent', methods=['POST'])
def registerStudent():
    request_data = request.get_json()
    message=db.registerStudent(request_data)
    return jsonify(message)


@register_routes.route('/getStudent')
def getStudent():

    request_data = request.get_json()
    student=db.getStudent(request_data)

    return jsonify(student)

# @register_routes.route('/getStudentList')
# def getStudentList():
#     # request_data = request.get_json()
#     students=db.getStudentList()
#     return jsonify(students)