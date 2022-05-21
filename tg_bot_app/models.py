import os 

from dotenv import load_dotenv
from sqlalchemy import create_engine, Integer, String, \
    Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


load_dotenv()
db_login = os.getenv('DB_LOGIN')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

engine = create_engine(f'postgresql+psycopg2://{db_login}:{db_password}@localhost/{db_name}', 
    echo=True, pool_size=6, max_overflow=10, encoding='latin1'
)
Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'recipes'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    receipt = Column(String(4000), nullable=False)
    ingridients = relationship("Ingridient", backref = 'recipe')
    
class Ingridient(Base): 
    __tablename__= 'ingridients'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    proportions = Column(String(100), nullable=False)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))

Base.metadata.create_all(engine)
