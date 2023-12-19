from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from typing import Annotated
from datetime import timedelta

from app.config import log
from app.schemas import response_schemas, request_schemas
from app.core.dependencies import get_db
from app.core import crud
from app.config import settings

router = APIRouter()


@router.get("/check")
async def check():
    return "OK"


@router.get("/indexes")
async def get_active_indexes(
    date: str,
    db: Session = Depends(get_db),
):
    """
    Get active indexes
    """
    indexes = crud.get_indexes(db, date=date)
    return indexes
