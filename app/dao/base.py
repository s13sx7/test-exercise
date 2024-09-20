from sqlalchemy import insert, select, update
from app.database import async_session_maker

class BaseDAO():
    model = None
    
    @classmethod
    async def add_data(cls, **data):
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()
        
    @classmethod
    async def view_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns)
            result = await session.execute(query)
            return result.mappings().all()
        
    @classmethod
    async def find_one_or_none(cls, **filter):
        async with async_session_maker() as session:
            query = select(cls.model.__table__.columns).filter_by(**filter)
            result = await session.execute(query)
            return result.mappings().one_or_none()