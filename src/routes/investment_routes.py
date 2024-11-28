from fastapi import APIRouter, HTTPException, status
from schemas import InvestmentSchema
from repositories import investment_repository, owner_repository


investment_router = APIRouter(prefix='/investment', tags=['Investment'])

@investment_router.get('/{investment_id}', status_code=status.HTTP_200_OK)
def get_investment(investment_id: str):
    investment = investment_repository.find_investment_by_id(investment_id)
    if not investment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Investimento não encontrado.')
    return investment


@investment_router.post('/', status_code=status.HTTP_201_CREATED)
def create_investment(investment: InvestmentSchema):
    if not owner_repository.find_owner_by_id(investment.owner_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Proprietário não cadastrado.')
    investment_repository.save_investment(investment.model_dump())
    return investment
