from db import db_connection
from models import InvestmentModel

class InvestmentRepository:
    def __init__(self):
        pass

    @staticmethod
    def find_investment_by_id(investment_id:str) -> InvestmentModel:
        session = db_connection.db_session()
        investment = session.query(InvestmentModel).filter(
            InvestmentModel.id == investment_id
        ).first()
        session.close()
        return investment

    @staticmethod
    def save_investment(investment:dict):
        session = db_connection.db_session()
        session.add(InvestmentModel(**investment))
        session.commit()
        session.close()

investment_repository = InvestmentRepository()



