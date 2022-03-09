from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.schemas.sche_base import DataResponse
from app.schemas.sche_user import UserDetail
from app.services.srv_user import UserService

router = APIRouter()


@router.post('')
def register(db: Session = Depends(deps.get_db), user: UserDetail = None):
    user = UserService.create_user(db=db, user=user)
    return DataResponse().success_response(data={'user_id': user.id})