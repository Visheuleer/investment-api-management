from sqlalchemy import Column, CHAR, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from models import Base
import uuid


class InvestmentModel(Base):
    __tablename__ = "investments"

    id = Column(CHAR(36), primary_key=True, default=lambda: str(uuid.uuid4()), index=True)
    owner_id = Column(CHAR(36), ForeignKey("owners.id"), nullable=False, index=True)
    name = Column(String(255), nullable=False, index=True)
    amount_invested = Column(Float, nullable=False, index=True)

    owner = relationship("OwnerModel", back_populates="investment")