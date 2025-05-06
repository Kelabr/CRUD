import psycopg2 
from psycopg2 import OperationalError
import os
from dotenv import load_dotenv

load_dotenv()

def connection():
    try:
        coon = psycopg2.connect(
            host=os.getenv('HOST'),
            dbname=os.getenv('DATABASE'),
            user=os.getenv('USER'),
            password=os.getenv('PASSWORD'),
            port=os.getenv('PORT')
        )
        return coon
    except OperationalError as e:
        print('Erro ao conectar ao Banco', e)
        return None