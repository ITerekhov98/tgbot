import os
from random import randint

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .models import Recipe, Ingridient

load_dotenv()
db_login = os.getenv('DB_LOGIN')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
engine = create_engine(f'postgresql+psycopg2://{db_login}:{db_password}@localhost/{db_name}')

def get_random_recipe():
    session = Session(bind=engine)
    rows_query = session.query(Recipe) 
    if rows_query.count() > 0: 
        rand_index = randint(0, rows_query.count()-1) 
        rand_reciept = rows_query.all()[rand_index]
        ingridients = {el.name: el.proportions for el in rand_reciept.ingridients}
        result_data = {
            'receipt_name': rand_reciept.name,
            'receipt': rand_reciept.receipt,
            'ingridients': ingridients
        }
        session.close()
        return result_data
    return None

def get_info_by_name(name:str):
    session = Session(bind=engine)
    recipe = session.query(Recipe).filter(Recipe.name.contains(name)).first()
    if recipe is None:
        return None
    ingridients = {el.name: el.proportions for el in recipe.ingridients}
    result_data = {
        'receipt_name': recipe.name,
        'receipt': recipe.receipt,
        'ingridients': ingridients
    }
    session.close()
    return result_data
