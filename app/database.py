from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


DATA_URL = 'postgresql+asyncpg://postgres:postgres@localhost:5432/postgres'

engine = create_async_engine(DATA_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    ...