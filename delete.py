import sqlite3

conn = sqlite3.connect('db/database_alunos.db')
cursor = conn.cursor()

cursor.execute("DROP TABLE Estudantes;")

