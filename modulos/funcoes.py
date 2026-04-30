alunos = []

#Verificação de existencia de cadastro
def verificacao():
    if len(alunos) == 0:
        print('Sem alunos Encontrados')
        return
    
#Cadastrar Aluno
def cadastrar():
    nome = input('Nome do Aluno: ')
    idade = int(input('Idade do Aluno: '))
    nota = float(input('Nota:'))
    dados = {
        "nome" : nome,
        "idade": idade,
        "nota" : nota
        }
    alunos.append(dados)

#listar Alunos
def listar():
    verificacao()
    for aluno in alunos:
        print(f'{'=' * 30}\nNome do aluno: {aluno["nome"]}\nIdade Aluno: {aluno["idade"]}\nNota:{aluno["nota"]}\n{'='*30}')

#Consultar Aluno
def consultar():
    verificacao()
    for aluno in alunos:
        aluno_desejado = input('Nome do Aluno: ')
        if aluno_desejado.lower() == aluno['nome'].lower():
            print(f'Nome: {aluno["nome"]} | Idade: {aluno["idade"]} | Nota: {aluno["nota"]}')
        else:
            print('Aluno não encontrado')
            break

#Remover Aluno
def remover():
    verificacao()
    for aluno in alunos:
        aluno_desejado = input('Nome do Aluno: ')
        if aluno_desejado.lower() == aluno['nome'].lower():
            alunos.remove(aluno)
            print('Aluno removido')
        else:
            print('Aluno não encontrado')
            break