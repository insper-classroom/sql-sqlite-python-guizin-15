import sqlite3

# Exercício de Python - Sqlite

# Conexão com o banco de dados dentro da pasta "db"
conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

# Vamos criar uma tabela chamada "Estudantes" com os seguintes campos:
# ID (chave primária) -  Criado automáticamente pela base de dados
# Nome
# Curso
# Ano de Ingresso

cursor.execute("""
CREATE TABLE IF NOT EXISTS Estudantes (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Curso TEXT NOT NULL,
    Ano_de_ingresso INTEGER
);
""")

Alunos = [
        ('Ana Silva', 'Computação', '2019'),
        ('Pedro Mendes', 'Física', '2021'),
        ('Carla Souza', 'Computação', '2020'),
        ('João Alves', 'Matemática', '2018'),
        ('Maria Oliveira', 'Química', '2022')
]

# cursor.executemany("""
# INSERT INTO Estudantes (Nome, Curso, 'Ano_de_ingresso')
# VALUES (?, ?, ?);
# """, Alunos)

conn.commit()

cursor.execute("SELECT * FROM Estudantes")

print(cursor.fetchall())
print()

#código para printar 2019 - 2020

cursor.execute("SELECT * FROM Estudantes WHERE Ano_de_ingresso = 2019 or Ano_de_ingresso = 2020")

print(cursor.fetchall())
print()

cursor.execute("UPDATE Estudantes SET Ano_de_ingresso = 2015 WHERE id = 1")

cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())
print()

cursor.execute("SELECT * FROM Estudantes WHERE Curso = 'Computação' AND Ano_de_ingresso > 2019")

print(cursor.fetchall())
print()


cursor.execute("UPDATE Estudantes SET Ano_de_ingresso = 2018 WHERE Curso = 'Computação'")

cursor.execute("SELECT * FROM Estudantes")
print(cursor.fetchall())
print()

