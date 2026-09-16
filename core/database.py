import os
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

Base = declarative_base()

class Incident(Base):
    __tablename__ = 'incidents'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    raw_data = Column(Text)
    executive_summary = Column(Text)
    technical_analysis = Column(Text)
    response_actions = Column(Text)
    status = Column(String(50), default="Draft")
    framework_mapping = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

def get_engine():
    db_path = os.path.join(os.getcwd(), 'incidents.db')
    return create_engine(f'sqlite:///{db_path}')

def init_db():
    engine = get_engine()
    Base.metadata.create_all(engine)
    return sessionmaker(bind=engine)()