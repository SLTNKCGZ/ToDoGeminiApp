from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey


class Todo(Base): #Todo adında bir class oluşturuyoruz ve Base classından miras alıyoruz.Neden Base classından miras aldık?Çünkü Base classı veritabanı tablolarını oluşturmak için kullanılır.
    __tablename__="todos"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    description=Column(String)
    priority = Column(Integer)
    complete=Column(Boolean,default=False)

    owner_id=Column(Integer,ForeignKey("users.id"))

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    email=Column(String,unique=True)
    username=Column(String,unique=True)
    first_name=Column(String)
    last_name=Column(String)
    hashed_password=Column(String)
    is_active=Column(Boolean,default=True)
    role=Column(String,default="user")
    phone_number=Column(String,unique=True)