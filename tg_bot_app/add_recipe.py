import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from .models import Recipe, Ingridient

load_dotenv()
db_login = os.getenv('DB_LOGIN')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
engine = create_engine(f'postgresql+psycopg2://{db_login}:{db_password}@localhost/{db_name}')

def add_recipe():
    recipe_name = input('Введите название блюда: ')
    receipt = input('Введите рецепт: ')
    recipe = Recipe(name = recipe_name, receipt=receipt)
    ingridients = []
    flag = input('Будете добавлять ещё ингридиенты? [y/n]')
    while flag == 'y':
        i = Ingridient(name=input('Введите название: '),
                       proportions = input('Введите количество: '),
                       recipe=recipe)
        ingridients.append(i)
        flag = input('Будете добавлять ещё ингридиенты? [y/n]')
    session = Session(bind=engine)
    session.add_all([recipe, *ingridients])    
    session.commit()   