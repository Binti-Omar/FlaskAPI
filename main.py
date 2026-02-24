# rules of a ReST API
# 1. Data is transferred as key value-pairs called JSON.Sending from JS as JSON Object and from python as dictionary
# 2. You must define routes/URL 
# 3. You must define a HTTP method(GET,POST,PUT,DELETE,PATCH)
# 4. You must define a status code(200,201,404,401,500)

from flask import Flask,jsonify,request
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base,User

app = Flask(__name__)

DATABASE_URL = "postgresql+psycopg2://postgres:C0717824020@localhost:5432/flask_api"

engine = create_engine(DATABASE_URL,echo=True)

session = sessionmaker(bind=engine)

mysession = session()

Base.metadata.create_all(engine)

allowed_methods = ["GET","POST","UPDATE","DELETE","PATCH"]
user_list = []

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
            return jsonify({"data":user_list}),200
        elif method == "post":
            data = request.get_json ()
            if data["name"] == "" or data["location"] =="":
                return jsonify({"msg":"name and location fields required"}),403
            else:
                # user_list.append(data)
                new_user = User(name = data["name"], location = data["location"])
                mysession.add(new_user)
                mysession.commit()
                return jsonify({"msg":"Successfully added user."}),201
        else:
            return jsonify({"msg":"Method not allowed"}),405
    except Exception as e:
        return jsonify({"error":str(e)}),500







app.run (debug=True)