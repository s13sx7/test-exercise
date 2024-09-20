from sqlalchemy import String, Date
from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column

class Passwords(Base):
    __tablename__='passwords'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_name: Mapped[str] = mapped_column(String(30),nullable=False)
    hashed_password: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[Date] = mapped_column(Date, nullable=False)
    updated_at:Mapped[str] = mapped_column(String, default='0')