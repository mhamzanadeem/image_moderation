from pydantic import BaseModel
from datetime import datetime

class TokenCreate(BaseModel):
    token: str
    isAdmin: bool

class TokenOut(BaseModel):
    token: str
    isAdmin: bool
    createdAt: datetime

class Usage(BaseModel):
    token: str
    endpoint: str
    timestamp: datetime
