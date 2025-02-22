from sqlalchemy import Column, Integer, String, JSON, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class QuizChatModel(Base):
    __tablename__ = "quiz_chat_master"  # Make sure the table name is correct

    id = Column(Integer, primary_key=True, autoincrement=True)
    quiz_notes = Column(JSON, nullable=False)
    active = Column(Boolean, default=True)
    created_on = Column(DateTime, default=datetime.utcnow)
    updated_on = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted_on = Column(DateTime, nullable=True)
