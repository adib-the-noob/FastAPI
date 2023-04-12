from fastapi import FastAPI
from models import User, Gender, Role
from uuid import uuid4, UUID
from pydantic import BaseModel
from typing import Optional, List


app = FastAPI()

db : List[User] = [
    User(
        id=uuid4(),
        first_name="John",
        last_name="Doe",
        gender = Gender.male,
        roles = [Role.student, Role.user],
        email = "hell@aadib,com"
        ),
    User(
        id=uuid4(),
        first_name="Jane",
        last_name="Doe",
        gender=Gender.female,
        email="hellow@gmail.com",
        roles=[Role.student, Role.admin],
        )
]

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get('/users')
async def get_users():
    return db

@app.post('/create-user')
async def create_user(user: User):
    db.append(user)
    return {
        'id' : user.id,
        'message' : 'User created successfully'
    }

@app.delete('/user/{user_id}')
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {
                'id' : user.id,
                'message' : 'User deleted successfully'
            }
    return {
        'message' : 'User not found'
    }