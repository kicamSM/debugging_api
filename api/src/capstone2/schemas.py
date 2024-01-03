from pydantic import BaseModel, EmailStr, field_validator, Field
import os
print("os.getcwd() in schemas.py:", os.getcwd())


class UserPost(BaseModel): 
    username: str
    password: str
    email: str
    user_id: int