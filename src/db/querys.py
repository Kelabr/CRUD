def inserir_user(coon, name, email, password):
    with coon.cursor() as cur:
        cur.execute('INSERT INTO users (name, email, password) VALUES (%s, %s, %s)', (name, email, password))
    coon.commit()
