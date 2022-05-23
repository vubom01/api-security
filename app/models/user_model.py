import json

from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer

from app.models.base_model import BareBaseModel


class User(BareBaseModel):
    __tablename__ = "users"

    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    dob = Column(String, nullable=True)

    def public_info_to_client(self) -> dict:
        return {
            'title': self.title,
            'type': self.type,
            'choices': json.loads(self.content).get('choices'),
            'duration': self.duration
        }
