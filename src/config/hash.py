from passlib.context import CryptContext

ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"
SECRET_KEY = "joseaimelesfrite"


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")