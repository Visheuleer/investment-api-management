from db import db_connection
from models import OwnerModel

class OwnerRepository:
    def __init__(self):
        pass

    @staticmethod
    def find_owner_by_document(document:str) -> OwnerModel:
        session = db_connection.db_session()
        owner = session.query(OwnerModel).filter(
            OwnerModel.document == document
        ).first()
        session.close()
        return owner

    @staticmethod
    def save_owner(owner:dict):
        session = db_connection.db_session()
        session.add(OwnerModel(**owner))
        session.commit()
        session.close()



