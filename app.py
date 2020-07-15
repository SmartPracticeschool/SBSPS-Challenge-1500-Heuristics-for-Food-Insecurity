from flask import Flask, jsonify,request
from flask_cors import CORS, cross_origin
import database as db

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({"message" : "YOUR APIs are RUNNING "})

@app.route('/userregister' , methods = ['POST'])
def UserRegister():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    address = request.form['address']
    pincode = request.form['pincode']
    phone_number = request.form['phone_number']
    if(db.register_user(first_name,last_name,email,password,address,pincode,phone_number)):
        return jsonify({"res":"success"}),200
    else:
        return jsonify({"res" : "fail"}),400

@app.route('/userlogin')
def UserLogin():
    username = request.form['username']
    last_name = request.form['password']
    pass

@app.route('/retailerregister' , methods = ['POST'])
def RatailerRegister():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    retail_shop_name = request.form['shop_name']
    email = request.form['email']
    password = request.form['password']
    address = request.form['address']
    pincode = request.form['pincode']
    phone_number = request.form['phone_number']
    if(db.register_retail(first_name,last_name,retail_shop_name,email,password,address,pincode,phone_number)):
        return jsonify({"res":"success"}),200
    else:
        return jsonify({"res" : "fail"}),400

@app.route('/retailerlogin')
def RetailerLogin():
    pass

@app.route('/additem' , methods = ['POST'])
def AddItem():
    product_name = request.form['product_name']
    product_price = request.form['product_price']
    product_description = request.form['product_description']
    product_image = request.form['product_image']
    if(db.insert_product(product_name,product_description,product_price,product_image)):
        return jsonify({"res" : "success"}),200
    else:
        return jsonify({"res" : "fail"}),400


@app.route('/itemdetails')
def AllItemDetails():
    pass

@app.route('/searchitem/<name>')
def SearchItem(name):
    pass


    


if __name__ == "__main__":
    app.run(debug=True)
