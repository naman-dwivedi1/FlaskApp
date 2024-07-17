from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
import json

import pymysql
pymysql.install_as_MySQLdb()

password='Enemendwdi1001'
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{password}@localhost:3306/FlaskApp'
db = SQLAlchemy(app)

@app.route("/",methods=["GET"])
def Welcome():
    return "Welcome to our APP"

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50),nullable=False)
    email = db.Column(db.String(120), unique=True , nullable=False)
    password = db.Column(db.String(120),nullable=False)
    
@app.route("/addUser", methods=["POST"])
def addUser():
    data=request.json
    newUser=User(firstname=data['firstname'],lastname=data['lastname'],email=data['email'],password=data['password'])
    db.session.add(newUser)
    db.session.commit()
    return "User Added Successfully"

@app.route("/readAllUsers",methods=["GET"])
def readAllUsers():
    users = User.query.all()
    return jsonify([{
        "id": user.id,
        "firstname": user.firstname,
        "lastname": user.lastname,
        "email": user.email,
        "password": user.password,
    } for user in users])

@app.route("/updateUser/<int:id>",methods=["PUT"])
def updateUser(id):
    user=User.query.get(id)
    data=request.json
    for key, value in data.items():
        if hasattr(user, key):
            setattr(user, key, value)
    db.session.commit()
    return "User Updated Successfully"

@app.route("/updateSomeInfo/<int:id>",methods=["PATCH"])
def updateSomeInfo(id):
    user=User.query.get(id)
    data=request.json
    for key, value in data.items():
        if hasattr(user, key):
            setattr(user, key, value)
    db.session.commit()
    return "User Info Updated Successfully"

@app.route("/deleteUser/<int:id>",methods=["DELETE"])
def deleteUser(id):
    user=User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return "User Deleted Successfully"

@app.errorhandler(400)
def page_not_found(error):
    return "Client Side Error"

@app.errorhandler(500)
def page_not_found(error):
    return "Server Side Error"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

