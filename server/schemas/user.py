import pydantic
from bson.objectid import ObjectId
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str
from server.config.db import conn

def recommend_product(item) ->dict:
    return {
        "_id":item["_id"],
        "category":[conn.petstore.categories.find_one({"_id":i}) for i in item["categories"]],
        "name":item["name"],
        "price":item["price"],
        "images":[conn.petstore.images.find_one({"_id":i}) for i in item["images"]]
    }

