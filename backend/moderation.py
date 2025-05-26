from fastapi import APIRouter, UploadFile, HTTPException, Header
from .database import db
from .utils import dummy_moderation
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

def verify_token(authorization: str = Header(...)) -> str:
    if not authorization.startswith("Bearer "):
        logger.error("Invalid authorization header format")
        raise HTTPException(status_code=401, detail="Invalid token")
    token = authorization[len("Bearer "):].strip()
    if token != "isAdmin":
        logger.error(f"Invalid token: {token}")
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@router.post("/moderate")
async def moderate_image(image: UploadFile, token: str = Header(...)):
    try:
        logger.info(f"Received file: {image.filename}, token: {token}")
        content = await image.read()
        result = dummy_moderation(content)
        logger.info(f"Moderation result: {result}")
        db["usages"].insert_one({
            "token": token,
            "endpoint": "moderate",
            "timestamp": datetime.utcnow()
        })
        return result
    except Exception as e:
        logger.error(f"Error in moderate_image: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")