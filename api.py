from flask import Flask, jsonify, request
import util as myutil
from load_money import loadmoney_routes
from register import register_routes
from upload import upload_routes
app = Flask(__name__)
app.register_blueprint(loadmoney_routes)
app.register_blueprint(register_routes)
app.register_blueprint(upload_routes)
app.run(port=5000)