# rules of a ReST API
# 1. Data is transferred as key value-pairs called JSON.Sending from JS as JSON Object and from python as dictionary
# 2. You must define routes/URL 
# 3. You must define a HTTP method(GET,POST,PUT,DELETE,PATCH)
# 4. You must define a status code(200,201,404,401,500)

from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
    return jsonify({"Flask API Version":"1.0"}),200



app.run ()