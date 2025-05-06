def inserir_user(coon, name, email, password):
    with coon.cursor() as cur:
        cur.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', (name, email, password))
    coon.commit()

def delete(coon, name):
    with coon.cursor() as cur:
        cur.execute('DELETE FROM users WHERE name = %s', (name,))
    coon.commit()
