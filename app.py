from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy

import re

import pymysql
pymysql.install_as_MySQLdb()

password='Enemendwdi1001'
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:{password}@localhost:3306/FlaskApp'
db = SQLAlchemy(app)

regex=r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

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
    
fields=['firstname','lastname','email','password']
    
@app.route("/user", methods=["GET","POST","PUT","PATCH","DELETE"])
def user():
    if(request.method=="GET"):
        try:
            args = request.args
            if len(args) == 0:
                users=User.query.all()
                return jsonify([{
                    "id": user.id,
                    "firstname": user.firstname,
                    "lastname": user.lastname,
                    "email": user.email,
                    "password": user.password,
                } for user in users])
            else:
                try:
                    user=User.query.filter_by(email=args['email']).first()
                except: return jsonify({'error': 'Give correct key as email in params'}), 400
                if user:
                    return jsonify({
                        "id": user.id,
                        "firstname": user.firstname,
                        "lastname": user.lastname,
                        "email": user.email,
                        "password": user.password,
                    })
                else: return jsonify({'error': 'User with this email does not exists'}), 400
        except:
            return jsonify({'error': "Internal Server Error"}), 500
    elif(request.method=="POST"):
        try:
            try:
                data=request.json
            except: return jsonify({'error': "Please provide all necessary user details to add user in the database"}), 400
            try: 
                user=User.query.filter_by(email=data['email']).first()
            except: return jsonify({'error': 'Give correct key as email in body'}), 400
            if user: return jsonify({'error': 'User already exists'}), 400
            else:
                if(re.fullmatch(regex, data["email"])==None): return jsonify({'error': 'Incorrect Email format'}), 400
                newUser=User()
                for key,value in data.items():
                    setattr(newUser,key,value)
                db.session.add(newUser)
                db.session.commit()
                return "User Added Successfully", 200
        except:
            return jsonify({'error': "Internal Server Error"}), 500
    elif(request.method=="PUT"):
        try:
            args=request.args
            if len(args) == 0: return jsonify({'error': "Please provide email of the user to be updated"}), 400
            try:   
                data=request.json
            except: return jsonify({'error': "Please provide some fields to update"}), 400
            try:
                user=User.query.filter_by(email=args["email"]).first()
            except: return jsonify({'error': 'Give correct key as email in params'}), 400
            if user:  
                for key, value in data.items():
                    if hasattr(user, key)==False:
                        return jsonify({'error': "No such field exists to update"}), 400
                    else:
                        if(getattr(user,key)!=value):
                            setattr(user, key, value)
                db.session.commit()
                return "User Updated Successfully", 200
            else: return jsonify({'error': 'User with this email does not exists'}), 400
        except:
            return jsonify({'error': "Internal Server Error"}), 500
    elif(request.method=="PATCH"):
        try:
            try:
                data=request.json
            except: return jsonify({'error': "Please provide some fields to update"}), 400
            args=request.args
            if len(args) == 0:
                try:
                    user=User.query.filter_by(email=data['email']).first()
                except: return jsonify({'error': "Please provide correct key as email in body"}), 400
                if user:
                    for key, value in data.items():
                        if hasattr(user, key)==False:
                            return jsonify({'error': "No such field exists to update"}), 400
                        else:
                            if(getattr(user,key)!=value):
                                setattr(user, key, value)
                    db.session.commit()
                    return "User Patched Updated Successfully", 200
                else:
                    if(re.fullmatch(regex, data["email"])==None): return jsonify({'error': 'Incorrect Email format'}), 400
                    newUser=User()
                    keys=data.keys()
                    for field in fields:
                        if field not in keys: return jsonify({'error': "Please provide all the fields that are necessary"}), 400
                    for key,value in data.items():
                        if hasattr(newUser, key)==False:
                            return jsonify({'error': "No such field exists to update"}), 400
                        setattr(newUser,key,value)
                    db.session.add(newUser)
                    db.session.commit()
                    return "User Patched Added Successfully", 200
            else:
                try:
                    user=User.query.filter_by(email=args['email']).first()
                except: return jsonify({'error': 'Please provide correct key as email in params'}), 400
                if user:
                    for key, value in data.items():
                        if hasattr(user, key)==False:
                            return jsonify({'error': "No such field exists to update"}), 400
                        else:
                            if(getattr(user,key)!=value):
                                setattr(user, key, value)
                    db.session.commit()
                    return "User Patched Updated Successfully", 200
                else: return jsonify({'error': 'User with this email does not exists'}), 400
        except:
            return jsonify({'error': "Internal Server Error"}), 500
    elif(request.method=="DELETE"):
        try:
            args=request.args
            if len(args) == 0: return jsonify({'error': "Please provide email of the user to be deleted"}), 400
            else:
                try:
                    user=User.query.filter_by(email=args["email"]).first()
                except: return jsonify({'error': 'Please provide correct key as email in params'}), 400
                if user:
                    db.session.delete(user)
                    db.session.commit()
                    return "User Deleted Successfully", 200 
                else: return jsonify({'error': 'User with this email does not exists'}), 400
        except:
            return jsonify({'error': "Internal Server Error"}), 500
    else: return "Unknown type of method request"
    
# @app.errorhandler(400)
# def page_not_found(error):
#     return "Client Side Error"

# @app.errorhandler(500)
# def page_not_found(error):
#     return "Server Side Error"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)

