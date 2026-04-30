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
    aluno_desejado = input('Nome do Aluno: ')
    for aluno in alunos:
        if aluno_desejado.lower() == aluno['nome'].lower():
            print(f'Nome: {aluno["nome"]} | Idade: {aluno["idade"]} | Nota: {aluno["nota"]}')
            break
    else:
        print('Aluno não encontrado')
            

#Remover Aluno
def remover():
    verificacao()
    aluno_desejado = input('Nome do Aluno: ')
    for aluno in alunos:    
        if aluno_desejado.lower() == aluno['nome'].lower():
            alunos.remove(aluno)
            print('Aluno removido')
            break
    else:
        print('Aluno não encontrado')
            

