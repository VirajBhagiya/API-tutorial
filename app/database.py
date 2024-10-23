from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
import time
from psycopg2.extras import RealDictCursor
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'

# connect_args = {"check_same_thread": False}
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    
# class posts(SQL, table=True):
#     id: int = Field(default=None, primary_key=True)
#     title: str = Field(index=True)
#     content: str = Field(index=True)
#     published: bool | None = Field(default="True")
#     created_at: datetime = Field(default=datetime.now())



# while True:
#     try:
#         conn = psycopg2.connect(host='<database_hostname>', database='<database_name>', user='<database_username>', password=<database_password>, cursor_factory=RealDictCursor)
        
#         cur = conn.cursor()
#         print('\nConnection Successful!!\n')
#         break
#     except Exception as e:
#         print("Connection to database failed!! Retrying in 2 seconds...")
#         print("Error: ", e)
#         time.sleep(2)