from sqlalchemy import update
from sqlalchemy.orm import Session
from sqlalchemy.exc import NoResultFound

from typing import Union

from app.models import db_models, models
from app.schemas import response_schemas, request_schemas
from app.config import log


def get_indexes(db: Session):
    indexes = db.query(
        db_models.ActiveIndex.active_id,
        db_models.ActiveIndex.sensors_id,
        db_models.ActiveIndex.value,
        db_models.ActiveIndex.measurement_date,
    ).all()

    return indexes
