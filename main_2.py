from db.db_utils import *


campos = "Nome TEXT, Curso TEXT, Ano_de_Ingresso INTEGER"
cria_tabela("Estudantes", campos)

registros = [
    ('Ana Silva', 'Computação', 2019),
    ('Pedro Mendes', 'Física', 2021),
    ('Carla Souza', 'Computação', 2020),
    ('João Alves', 'Matemática', 2018),
    ('Maria Oliveira', 'Química', 2022)
]
inserir("Estudantes", registros, ('Nome', 'Curso', 'Ano_de_Ingresso'))

print("Todos os registros:")
todos_registros = consultar_registros("Estudantes")
for registro in todos_registros:
    print(registro)

print("\nRegistros consultados:")
estudantes_2019_2020 = consultar_registros("Estudantes WHERE Ano_de_Ingresso BETWEEN 2019 AND 2020")
for registro in estudantes_2019_2020:
    print(registro)

atualiza("Estudantes", 3, {"Ano_de_Ingresso": 2018})

print("\nApós atualização:")
todos_registros = consultar_registros("Estudantes")
for registro in todos_registros:
    print(registro)

delete("Estudantes", 2)

print("\nApós exclusão:")
todos_registros = consultar_registros("Estudantes")
for registro in todos_registros:
    print(registro)

print("\nEstudantes de Computação que ingressaram após 2019:")
estudantes_computacao_apos_2019 = consultar_registros("Estudantes WHERE Curso = 'Computação' AND Ano_de_Ingresso > 2019")
for registro in estudantes_computacao_apos_2019:
    print(registro)

atualiza("Estudantes", 1, {"Ano_de_Ingresso": 2018})

print("\nApós correção dos registros de Computação:")
todos_registros = consultar_registros("Estudantes")
for registro in todos_registros:
    print(registro)