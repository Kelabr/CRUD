from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from schema import New_user, Name
from src.db.connection import connection
from src.db.querys import inserir_user, delete #Função que retorna uma query 

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

@router.delete('/user')
def delete_user(name:Name = Body(...)):
    try:
        delete(coon, name.name)
        return {'menssage':'Usuáro deletado (x)'}
    except Exception as e:
        return{'menssage':f'Erro ao tentar deletar usuário!! {e}'}