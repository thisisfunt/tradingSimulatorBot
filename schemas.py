from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.types import String, Float, Integer
from sqlalchemy import create_engine
from dotenv import dotenv_values

CONNECTION_REF = dotenv_values(".env")["connection_ref"]
engine = create_engine(CONNECTION_REF)

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


class User(Base):
    __tablename__="user"
    tg_id: Mapped[int] = mapped_column(Integer(), unique=True)
    amount: Mapped[float] = mapped_column(Float())

if __name__ == "__main__":
    Base.metadata.create_all(engine)

