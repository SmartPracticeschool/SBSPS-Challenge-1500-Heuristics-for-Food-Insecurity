from pymongo import MongoClient
import pymongo
import uuid

client = pymongo.MongoClient("mongodb+srv://react:react@malya-gso2y.mongodb.net/<dbname>?retryWrites=true&w=majority")

db = client.covid_food

def register_user(f_name,l_name,email,password,address,pincode,phno):
    collection = db.user
    u_id = uuid.uuid4().hex[:20]
    u_id = u_id[:len((f_name))]
    data = {"f_name" : f_name,
        "l_name" : l_name,
        "u_id" : u_id,
        "phno" : phno,
        "pincode" : pincode,
        "address" : address,
        "email" : email,
        "password" : password
    }
    response = collection.insert_one(data)
    if(response.inserted_id):
        return True
    else:
        return False

def register_retail(f_name,l_name,retail_shop_name,email,password,address,pincode,phno):
    collection = db.retailer
    r_id = uuid.uuid4().hex[:20]
    r_id = r_id[:len(f_name)]
    data = {"f_name" : f_name,
        "l_name" : l_name,
        "r_id" : r_id,
        "shop_name" : retail_shop_name,
        "phno" : phno,
        "pincode" : pincode,
        "address" : address,
        "email" : email,
        "password" : password
    }
    response = collection.insert_one(data)
    if(response.inserted_id):
        return True
    else:
        return False
    
def insert_product(product_name,product_description,product_price,product_image):
    collection = db.items
    product_id = uuid.uuid4().hex[:20]
    product_id = product_id[:len(product_name)]
    data = { "product_name" : product_name,
             "product_id" : product_id,
             "product_image" : product_image,
             "product_price" : product_price,
             "product_des" : product_description
    }
    response = collection.insert_one(data)
    if(response.inserted_id):
        return True
    else:
        return False
