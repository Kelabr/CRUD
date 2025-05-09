from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from schema import New_user, Name
from src.db.connection import connection
from src.db.querys import inserir_user, delete, update, getUser #Função que retorna uma query 

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

@router.put('/user')
def update_user(update_user:New_user):
    try:
        update(coon, update_user.name, update_user.email, update_user.password)
        return {'Menssage':'Usuário Atualizado'}
    except Exception as e:
        return{'menssage':f'Erro ao atualizar {e}'}

@router.get('/user')
def getuser():
    try:
        response = getUser(coon)
        return response
    except Exception as e:
        return{'menssage':f'Erro ao buscar usuários - {e}'}

