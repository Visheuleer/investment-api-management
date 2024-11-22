from sqlalchemy import Column, CHAR, String
from models import Base
import uuid


class OwnerModel(Base):
    __tablename__ = "owners"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    fullname = Column(String(255), nullable=False, index=True)
    document = Column(String(11), nullable=False, unique=True, index=True)