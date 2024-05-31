usuarios = []
livros = []

def menu_principal():
    while True:
        print("\nBem vindo! Escolha uma das opções abaixo:")
        print("1. Login")
        print("2. Gerenciar usuários")
        print("3. Cadastrar livros")
        print("4. Buscar livros")
        print("5. Sair")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            login()
        elif opcao == '2':
            gerenciar_usuarios()
        elif opcao == '3':
            cadastrar_livros(livros)
        elif opcao == '4':
            buscar_livros()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

def login():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha: ")
    for usuario in usuarios:
        if usuario['usuario'] == nome and usuario['senha'] == senha:
            print(f"Bem-vindo, {nome}!")
            return
    print("Usuário ou senha incorretos. Tente novamente.")

def cadastrar_livros(livros):
    print("Cadastrar livros")
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o nome do autor do livro: ")
    ano = input("Digite o ano de publicação do livro: ")
    livros.append({'titulo': titulo, 'autor': autor, 'ano': ano})
    print(f"Livro '{titulo}' cadastrado com sucesso!")

def buscar_livros():
    print("Buscar livros")
    criterio = input("Você quer buscar por título, autor ou ano? ").lower()
    termo = input(f"Digite o {criterio} que deseja buscar: ")

    resultados = []
    for livro in livros:
        if criterio == 'título' and termo.lower() in livro['titulo'].lower():
            resultados.append(livro)
        elif criterio == 'autor' and termo.lower() in livro['autor'].lower():
            resultados.append(livro)
        elif criterio == 'ano' and termo == livro['ano']:
            resultados.append(livro)

    if resultados:
        print("Livros encontrados:")
        for livro in resultados:
            print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")
    else:
        print(f"Nenhum livro encontrado para o {criterio} '{termo}'.")

def gerenciar_usuarios():
    while True:
        print("\n-------------------------------")
        print("ESCOLHA A OPÇÃO DESEJADA")
        print("1. Cadastrar usuário")
        print("2. Gerar relatórios de usuários")
        print("3. Gerar relatórios de livros")
        print("4. Voltar ao menu principal")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            cadastrar_usuario()
        elif opcao == '2':
            gerar_relatorios_usuarios()
        elif opcao == '3':
            gerar_relatorios_livros()
        elif opcao == '4':
            break
        else:
            print("Opção inválida, tente novamente.")

def cadastrar_usuario():
    nome = input("Digite o nome do usuário: ")
    senha = input("Digite a senha para cadastro: ")
    usuarios.append({'usuario': nome, 'senha': senha})
    print(f"Usuário {nome} com senha {senha} cadastrado com sucesso!")

def gerar_relatorios_usuarios():
    print("Segue lista com relatórios de usuários")
    for usuario in usuarios:
        print(usuario)

def gerar_relatorios_livros():
    print("Lista de livros cadastrados:")
    for livro in livros:
        print(f"Título: {livro['titulo']}, Autor: {livro['autor']}, Ano: {livro['ano']}")

menu_principal()
