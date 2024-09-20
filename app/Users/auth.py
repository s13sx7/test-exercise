from random import choice
import string
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import jwt
from app.Users.dao import UsersDAO

def generate_password(length):
    char = string.ascii_letters+string.digits+string.punctuation
    password = ''.join([choice(char) for i in range(length)])
    
    return password

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def hashed_password(password):
    return pwd_context.hash(password)

def create_jwt_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now()+timedelta(minutes=30)
    to_encode.update({'exp': expire})
    encodet_jwt = jwt.encode(to_encode, key='ImTheGREATEST',algorithm='HS256')
    return encodet_jwt

def chek_pass(password:str, hashed_password:str) -> bool:
    return pwd_context.verify(secret=password, hash=hashed_password)

def authentication(name:str, password:str):
    user = UsersDAO.find_one_or_none(user_name=name)
    if not user and not chek_pass(password=password, hashed_password=user.hashed_password):
        return None
    return user