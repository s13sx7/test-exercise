from sqlalchemy import update
from app.dao.base import BaseDAO
from app.Users.models import Passwords
from app.database import async_session_maker


class UsersDAO(BaseDAO):
    model = Passwords
    
    @classmethod
    async def update(cls, name:str, password:str, date):
        async with async_session_maker() as session:
            query = (
                update(cls.model)
                .where(cls.model.user_name == name)
                .values(hashed_password=password, updated_at=date)
            )
            await session.execute(query)
            await session.commit()