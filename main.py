# rules of a ReST API
# 1. Data is transferred as key value-pairs called JSON.Sending from JS as JSON Object and from python as dictionary
# 2. You must define routes/URL 
# 3. You must define a HTTP method(GET,POST,PUT,DELETE,PATCH)
# 4. You must define a status code(200,201,404,401,500)

from flask import Flask,jsonify,request
from sqlalchemy import create_engine,select
from sqlalchemy.orm import sessionmaker
from database import User, Base
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

DATABASE_URL = "postgresql+psycopg2://postgres:C0717824020@localhost:5432/vuemyduka"

# Connecting SQLAlchemy to PostgerSql using engine function
engine = create_engine(DATABASE_URL,echo=False)

# Create  a session to call query methods
session = sessionmaker(bind=engine)
mysession = session()

# Create tables automatically
Base.metadata.create_all(engine)

allowed_methods = ["GET","POST","DELETE","PATCH"]

@app.route("/",methods = allowed_methods)
def home():
    method = request.method.lower()
    if method == "get":
        return jsonify({"Flask API Version":"1.0"}),200
    else:
        return jsonify({"msg":"Method not allowed"}),405
    
@app.route("/users",methods=allowed_methods)
def users():
    try:
        method = request.method.lower()
        if method == "get":
            user_list = []
            query =select(User)
            myusers = list(mysession.scalars(query).all())
            # print (users)

            for user in myusers:
                user_list.append({"id" : user.id,
                                  "name" :  user.name ,
                                  "location" : user.location})
                
            return jsonify({"data":user_list}),200
        elif method == "post":
            # Convert JSON to Dictionary
            data = request.get_json ()
            # Check if all fields are received
            if data["name"] == "" or data["location"] =="":
                return jsonify({"msg":"name and location fields required"}),403
            else:
                # user_list.append(data)/store user in users table using SQLAlchemy
                new_user = User(name = data["name"], location = data["location"])
                mysession.add(new_user)
                mysession.commit()
                return jsonify({"msg":"Successfully added user {data['name']}."}),201
        else:
            return jsonify({"msg":"Method not allowed"}),405
    except Exception as e:
        return jsonify({"error":str(e)}),500

@app.route('/register', methods= allowed_methods)
def register():
    data = request.get_json
    
    if data["username"] == "" or data["email"] == "" or data["password"]:
            return jsonify({ "error": "Name and Location cannot be empty" }), 400
    else:
        new_user = User(username=data["username"], email=data["email"], password=data["password"])
        mysession.add(new_user)
        mysession.commit()
        return jsonify({ "message": f"User created successfully{data['username']}" }), 201

app.run (debug=True)


