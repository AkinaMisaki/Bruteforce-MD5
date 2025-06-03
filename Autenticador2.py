import hashlib
import os

nome = 0
senha = 0
senha_hash = 0
nome = ''
senha = ''
lista = "!@#$%¨&*({[]})<>,.;/"

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
passwd_dir = os.path.join(__location__, 'usuarios.txt')

def input_usuario():
    global nome, senha
    while len(nome) != 4 or len(senha) != 4 or lista not in senha:
            
            nome = input("Digite o nome do usuario: ")

            if len(nome) != 4:
                print("Nome deve ter 4 caracteres.")
                continue

            senha = input("Digite a senha do usuario: ")

            if lista not in senha or len(senha)!= 4:
                print("Senha deve ter 4 caracteres e algum caracter especial.")
                continue

def cadastrar_usuario(nome, senha):

    senha_hash = hashlib.md5(senha.encode()).hexdigest()

    with open(passwd_dir, 'a') as f:
        f.write(f"{nome},{senha_hash}\n")

    print("Usuario cadastrado com sucesso.")

def autenticar_usuario(nome, senha):

    try:
        with open(passwd_dir, 'r') as f:
            for x in f:
                n, s = x.strip().split(',')
                if n == nome and hashlib.md5(senha.encode()).hexdigest() == s:
                    print("Autenticaçao bem-sucedida.")
                    return
            print("Nome ou senha incorretos.")
            
    except FileNotFoundError:
        print("Arquivo de usuarios não encontrado.")

while True:
    print("1. Cadastrar usuarioz\n2. Autenticar usuario\n3. Sair")
    opcao = input("Escolha uma opção: ")
    if opcao == '1':

        input_usuario()
        cadastrar_usuario(nome, senha)
        
    elif opcao == '2':

        input_usuario()
        autenticar_usuario(nome, senha)

    elif opcao == '3':
        exit()

    else:
        print("Opçao invalida.")