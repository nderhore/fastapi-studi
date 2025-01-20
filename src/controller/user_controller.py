from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.config.hash import pwd_context
from src.model.user import User
from src.service.auth_service import get_user_by_username
from src.schema.user_schema import UserCreate
from src.service.token_service import create_token


def create_user(user: UserCreate, db: Session):
    db_user = get_user_by_username(db=db,
                                   username=user.username)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nom d'utilisateur deja utilisé."
        )
    hashed_password = pwd_context.hash(user.password)
    new_user = User(username=user.username,
                    hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def login_user(user: UserCreate, db: Session):

    #1. je récupère mon utilisateur en base
    db_user = get_user_by_username(db=db,
                                   username=user.username)
    #2. je verifie qu'il n'est pas "None"
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Nom d'utilisateur non existant."
        )
    #3. je compare le password
    if pwd_context.verify(user.password, db_user.hashed_password):
        return create_token(data={"sub": user.username})
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Mot de passe incorrect."
        )
