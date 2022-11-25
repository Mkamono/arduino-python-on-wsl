from sqlalchemy import Column, Integer, String, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta, timezone

Base = declarative_base()


class Result(Base):
    JST: timezone = timezone(timedelta(hours=+9), 'JST')
    __tablename__ = 'serial_result'
    id: Column = Column(Integer, primary_key=True, autoincrement=True)
    message: Column = Column(String(200), nullable=False)
    created: Column = Column('created', DATETIME,
                             default=datetime.now(JST), nullable=False)
