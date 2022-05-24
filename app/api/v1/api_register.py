import random

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api import deps
from app.helpers.constant import LENGTH_OF_TERMINAL_CODE, LETTERS
from app.schemas.sche_base import DataResponse
from app.schemas.sche_user import UserCreateRequest, UserCreate
from app.services.srv_user import UserService

router = APIRouter()


def random_code() -> str:
    random_string = ""
    for number in range(LENGTH_OF_TERMINAL_CODE):
        random_string += random.choice(LETTERS)
    return random_string


@router.post('')
def register(db: Session = Depends(deps.get_db), user: UserCreateRequest = None):
    request = UserCreate(**user.dict())
    request.id = random_code()
    request.role = 'guest'
    user = UserService.create_user(db=db, user=request)
    return DataResponse().success_response(data={'user_id': user.id})
