from datetime import datetime
from fastapi import Request, HTTPException, status ,Depends
from jose import jwt, JWTError
from app.Users.dao import UsersDAO

def get_token(request:Request):
    token = request.cookies.get('access_token')
    if not token:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return token

async def get_current_user(token:str = Depends(get_token)):
    try:
        payload = jwt.decode(token, key='ImTheGREATEST', algorithms='HS256')
    except:
        raise JWTError
    expire: str = payload.get('exp')
    if not(expire) or int(expire) < datetime.now().timestamp():
        raise JWTError
    
    user_name: str = payload.get('sub')
    if not user_name:
        raise JWTError
    
    user = await UsersDAO.find_one_or_none(user_name=user_name)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    return user