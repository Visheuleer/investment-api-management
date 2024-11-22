from db import db_connection
from models import OwnerModel

class OwnerRepository:
    def __init__(self, owner: dict):
        self.owner = owner


    def find_owner_by_document(self) -> OwnerModel:
        session = db_connection.db_session()
        owner = session.query(OwnerModel).filter(
            OwnerModel.document == self.owner['document']
        ).first()
        session.close()
        return owner


    def save_owner(self):
        session = db_connection.db_session()
        session.add(OwnerModel(**self.owner))
        session.commit()
        session.close()



