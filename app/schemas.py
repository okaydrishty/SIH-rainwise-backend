from .database import Base, engine, Sessionlocal
from sqlalchemy import Column, Integer,String, Boolean, TIMESTAMP,text
from sqlalchemy.sql.expression import null
from typing import Optional

class User(Base):
    __tablename__="user_details"
    id= Column (Integer, primary_key=True, nullable=False)
    name=Column (String,nullable=False)
    email=Column (String,unique=True, nullable=False,index=True)
    password_hashed=Column(String, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True), nullable= False, server_default=text('now()'))
    
