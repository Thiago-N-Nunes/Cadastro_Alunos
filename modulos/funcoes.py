import sqlite3
import random

conexao = sqlite3.connect("../DB/alunos.db")
cursor = conexao.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS alunos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                serie TEXT,
                nota FLOAT
               )""")

conexao.commit( )

def gerar_cpf():
    cpf = random.randint((8),0,9)

# #Verificação de existencia de cadastro
# def verificacao():
#     if len(alunos) == 0:
#         print('Sem alunos Encontrados')
#         return
    
#Cadastrar Aluno
def cadastrar():
    nome = input('Nome do Aluno: ')
    idade = int(input('Idade do Aluno: '))
    nota = float(input('Nota:'))
    cursor.execute("INSERT INTO alunos (nome, idade, nota) VALUES (?, ?, ?)",(nome, idade,nota))
    conexao.commit()
    

# #listar Alunos
# def listar():
#     verificacao()
#     for aluno in alunos:
#         print(f'{'=' * 30}\nNome do aluno: {aluno["nome"]}\nIdade Aluno: {aluno["idade"]}\nNota:{aluno["nota"]}\n{'='*30}')

# #Consultar Aluno
# def consultar():
#     verificacao()
#     aluno_desejado = input('Nome do Aluno: ')
#     for aluno in alunos:
#         if aluno_desejado.lower() == aluno['nome'].lower():
#             print(f'Nome: {aluno["nome"]} | Idade: {aluno["idade"]} | Nota: {aluno["nota"]}')
#             break
#     else:
#         print('Aluno não encontrado')
            

# #Remover Aluno
# def remover():
#     verificacao()
#     aluno_desejado = input('Nome do Aluno: ')
#     for aluno in alunos:    
#         if aluno_desejado.lower() == aluno['nome'].lower():
#             alunos.remove(aluno)
#             print('Aluno removido')
#             break
#     else:
#         print('Aluno não encontrado')
            

