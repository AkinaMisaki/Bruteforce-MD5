import hashlib

nome = 0
senha = 0
senha_hash = 0

def cadastrar_usuario(nome, senha):
    if len(nome) != 4 or len(senha) != 4:
        print("Nome e senha devem ter 4 caracteres.")
        return
    senha_hash = hashlib.md5(senha.encode()).hexdigest()
    with open('usuarios.txt', 'a') as f:
        f.write(f"{nome},{senha_hash}\n")
    print("Usuario cadastrado com sucesso.")

def autenticar_usuario(nome, senha):
    try:
        with open('usuarios.txt', 'r') as f:
            for x in f:
                n, s = x.strip().split(',')
                if n == nome and hashlib.md5(senha.encode()).hexdigest() == s:
                    print("Autenticaçao bem-sucedida.")
                    return
            print("Nome ou senha incorretos.")
    except FileNotFoundError:
        print("Arquivo de usuarios não encontrado.")

while True:
    print("1. Cadastrar usuario")
    print("2. Autenticar usuario")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':
        nome = input("Digite o nome do usuario: ")
        senha = input("Digite a senha do usuario: ")
        cadastrar_usuario(nome, senha)
    elif opcao == '2':
        nome = input("Digite o nome do usuario: ")
        senha = input("Digite a senha do usuario: ")
        autenticar_usuario(nome, senha)
    elif opcao == '3':
        break
    else:
        print("Opçao invalida.")