from modulos import funcoes

while True:
    print('\nCadastro de alunos')
    opcoes = int(input('\n1 - Cadastrar Aluno\n2 - Listar Alunos\n3 - Consultar\n4 - Remover Aluno\n5 - Fechar\n'))
    match opcoes:
        case 1:
            funcoes.cadastrar()
        case 2:
            funcoes.listar()
        case 3:
            funcoes.consultar()
        case 4:
            funcoes.remover()
        case 5:
            break