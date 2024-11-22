from fastapi import APIRouter, HTTPException, status
from schemas import OwnerSchema
from repositories import OwnerRepository
from services import OwnerServices


owner_router = APIRouter(prefix='/owner', tags=['Owner'])
repository = OwnerRepository()

@owner_router.get('/{document}', status_code=status.HTTP_200_OK)
def get_owner(document: str):
    owner = repository.find_owner_by_document(document)
    if not owner:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'CPF: "{document}" não cadastrado.')
    return owner


@owner_router.post('/owner', status_code=status.HTTP_201_CREATED)
def create_owner(owner: OwnerSchema):
    if repository.find_owner_by_document(owner.document):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f'CPF "{owner.document}" já cadastrado.')
    if not OwnerServices(owner.document).document_is_valid():
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f'CPF "{owner.document}" inválido.')
    repository.save_owner(owner.model_dump())
    return owner
