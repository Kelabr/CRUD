from fastapi.responses import JSONResponse

def inserir_user(coon, name, email, password):
    with coon.cursor() as cur:
        cur.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', (name, email, password))
    coon.commit()

def delete(coon, name):
    with coon.cursor() as cur:
        cur.execute('DELETE FROM users WHERE name = %s', (name,))
    coon.commit()

def update(coon,name, new_email, new_password):
    with coon.cursor() as cur:
        cur.execute('UPDATE users SET email = %s, password = %s WHERE name = %s', (new_email, new_password, name))
    coon.commit()

def getUser(coon):
    with coon.cursor() as cur:
        cur.execute("SELECT * FROM users")
        resultado = cur.fetchall()

        colunas = [desc[0] for desc in cur.description]

        resultado_json = [dict(zip(colunas, linha)) for linha in resultado]
        return JSONResponse(content=resultado_json)