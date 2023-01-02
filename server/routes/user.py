from fastapi import APIRouter
from bson.objectid import ObjectId
from server.models.recommend import get_recommendations
from server.config.db import conn
from server.schemas.user import recommend_product
user=APIRouter()
import pydantic
pydantic.json.ENCODERS_BY_TYPE[ObjectId]=str

notes = {
    "1": {
        "title": "My first note",
        "content": "This is the first note in my notes application"
    },
    "2": {
        "title": "Uniform circular motion.",
        "content": "Consider a body moving round a circle of radius r, wit uniform speed v as shown below. The speed everywhere is the same as v but direction changes as it moves round the circle."
    }
}
@user.get("/")
async def get_notes() -> dict:
    return {
        "data": notes
    }

@user.get("/{id}")
async def get_note(id: str) -> dict:
    if int(id) > len(notes):
        return {
            "error": "Invalid note ID"
        }

    for note in notes.keys():
        if note == id:
            return {
                "data": notes[note]
            }


@user.put('/recommend')
async def find_recommend(id):
    result=get_recommendations(ObjectId(id))
    return [recommend_product(conn.petstore.products.find_one({"_id":i})) for i in result]
   

  