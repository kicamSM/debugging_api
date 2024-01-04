from pydantic import BaseModel

def schemas_func():
	print("schemas is importing")


class UserPost(BaseModel): 
    username: str
    password: str
    email: str
    user_id: int


