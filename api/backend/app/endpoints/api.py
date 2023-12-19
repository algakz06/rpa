from fastapi import APIRouter

from app.endpoints.indexes import router as indexes_router


router = APIRouter(
    prefix="/api",
    responses={404: {"description": "Not found"}},
)

router.include_router(indexes_router)
