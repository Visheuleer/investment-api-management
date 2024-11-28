from pydantic import BaseModel


class InvestmentSchema(BaseModel):
    owner_id: str
    name: str
    amount_invested: float

