from pydantic import BaseModel
from datetime import datetime

class UserSchema(BaseModel):
    email: str
    name: str
    stack: str

class ProfileResponse(BaseModel):
    status: str
    user: UserSchema
    timestamp: datetime
    fact: str
