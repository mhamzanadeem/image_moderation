from fastapi import APIRouter, Header, HTTPException
from models import TokenCreate
from database import tokens
from datetime import datetime

router = APIRouter(prefix="/auth")

def verify_admin(auth: str):
    token = auth.split(" ")[1]
    entry = tokens.find_one({"token": token, "isAdmin": True})
    if not entry:
        raise HTTPException(status_code=403, detail="Admin token required")

@router.post("/tokens")
def create_token(payload: TokenCreate, authorization: str = Header(...)):
    verify_admin(authorization)
    payload_dict = payload.dict()
    payload_dict["createdAt"] = datetime.utcnow()
    tokens.insert_one(payload_dict)
    return {"status": "token created"}

@router.get("/tokens")
def list_tokens(authorization: str = Header(...)):
    verify_admin(authorization)
    return list(tokens.find({}, {"_id": 0}))

@router.delete("/tokens/{token}")
def delete_token(token: str, authorization: str = Header(...)):
    verify_admin(authorization)
    tokens.delete_one({"token": token})
    return {"status": "token deleted"}
