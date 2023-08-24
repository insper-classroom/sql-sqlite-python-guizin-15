import sqlite3

conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

def cria_tabela(nome, fields):
    cursor.execute(f"DROP TABLE IF EXISTS {nome}")
    conn.commit()

    create_query = f"CREATE TABLE IF NOT EXISTS {nome} (ID INTEGER PRIMARY KEY AUTOINCREMENT, {fields})"
    cursor.execute(create_query)
    conn.commit()

def consultar_registros(nome):
    select_query = f"SELECT * FROM {nome}"
    cursor.execute(select_query)
    return cursor.fetchall()

def atualiza(nome, id_registro, fields):
    set_query = ""
    values = []

    for key, value in fields.items():
        set_query += f"{key} = ?, "
        values.append(value)

    set_query = set_query.rstrip(", ")
    values.append(id_registro)

    update_query = f"UPDATE {nome} SET {set_query} WHERE ID = ?"
    cursor.execute(update_query, values)
    conn.commit()

def delete(nome, id_registro):
    delete_query = f"DELETE FROM {nome} WHERE ID = ?"
    cursor.execute(delete_query, (id_registro,))
    conn.commit()

def inserir(nome, registros, campos):
    variaveis = ''
    
    for campo in campos:
        if campo == campos[len(campos)-1]:
            variaveis += '?'
        else:
            variaveis += '?, '

    cursor.executemany(f"""
    INSERT INTO {nome} {campos}
    VALUES ({variaveis});
    """, registros)

    conn.commit()