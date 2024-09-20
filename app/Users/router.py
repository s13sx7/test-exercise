from fastapi import APIRouter, Depends, HTTPException, status, Response
from datetime import datetime
from app.Users.schemas import SUser, SUpdate
from app.Users.dao import UsersDAO
from datetime import datetime
from app.Users.auth import hashed_password, authentication, create_jwt_token, generate_password
from app.Users.dependensies import get_current_user

router = APIRouter(prefix='/auth', tags=['Auth'])

@router.post('/registration')
async def reg_user(reg_data: SUser):
    date = datetime.now()
    exist_user = await UsersDAO.find_one_or_none(user_name=reg_data.name)
    if exist_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT)
    await UsersDAO.add_data(user_name=reg_data.name, hashed_password=hashed_password(reg_data.password), created_at=date)

@router.post('/login')
async def auth_user(response: Response, name:str, password:str):
    user = await authentication(name, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_jwt_token({'sub':str(user.user_name)})
    response.set_cookie('access_token', access_token, httponly=True)
    return access_token

@router.patch('/update_password')
async def update_password(data: SUpdate, user = Depends(get_current_user)):
    await UsersDAO.update(name=user.user_name, password=hashed_password(data.password), date=str(datetime.now()))

@router.get('/get_password')
async def get_password(user = Depends(get_current_user)):
    return user.hashed_password, 


@router.get('/all_users')
async def all_users():
    return await UsersDAO.view_all()


@router.get('/generate_password')
def generate_pass(lenght: int):
    return generate_password(length=lenght)