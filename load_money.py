from flask import Flask, jsonify, request
from flask import Blueprint
import money_dao  as db

#author:brini581
#Date:2023-01-29
#Desc:Money saving endpoint

loadmoney_routes = Blueprint("loadmoney_routes", __name__)

@loadmoney_routes.route('/getBalance')
def getStudentBalance():
    request_data = request.get_json()
    balance=db.getStudentBalance(request_data)

    return jsonify(balance)


@loadmoney_routes.route('/saveMoney', methods=['POST'])
def SaveStudentMoney():
    request_data = request.get_json()
    message=db.SaveStudentMoney(request_data)
    return jsonify(message)