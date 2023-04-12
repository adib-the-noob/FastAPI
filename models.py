from pydantic import BaseModel
from typing import Optional
from uuid import UUID, uuid4
from enum import Enum

class Gender(str, Enum):
    male = "Male"
    female = "Female"


class Role(str, Enum):
    admin = "admin"
    user = "user"
    student = "student"

class User(BaseModel):
    id : UUID = uuid4()
    first_name : str
    last_name : str
    email : str
    gender : Gender
    roles : list[Role]
    