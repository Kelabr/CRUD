from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schema import New_user
from src.db.connection import connection
from src.db.querys import inserir_user #Função que retorna uma query 

router = APIRouter()
coon = connection()

@router.get('/')
def test_api():
    return {'menssage':'Hello World!!'}

@router.post('/user')
def create_user(new_user:New_user):
    try:
        inserir_user(coon, new_user.name, new_user.email, new_user.password)
        return {'menssage':'Usuário registrado'}

    except:
        print('Erro ao cadastrar novo usuário')
