from sqlalchemy import Column, CHAR, String, Float, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models import Base
import datetime
import uuid


class InvestmentModel(Base):
    __tablename__ = "investments"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    owner_id = Column(CHAR(36), ForeignKey("owners.id"), nullable=False, index=True)
    name = Column(String(255), nullable=False, index=True)
    amount_invested = Column(Float, nullable=False, index=True)
    status = Column(Integer, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))

    owner = relationship("OwnerModel", back_populates="investment")