# Max Antonio e Luiz Henrique
import hashlib
import os
import itertools
import time

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) # Define o local para abrir o arquivo
passwd_dir = os.path.join(__location__, 'usuarios.txt')

def brute_force():

    fail = 0
    tenta = 0
    letters = [chr(i) for i in range(97, 123)]  # Adiciona letras minúsculas (a-z)

    with open(passwd_dir, 'r') as arquivo: # Abre o arquivo

        linha = arquivo.readline().strip()  # Pega a primeira linha

        while linha: 

            n, s = linha.split(',') # Separa o nome e a senha
            found = False 
            comeco = time.time() # Começa a contar o tempo

            if tenta > 0: # Usado para decidir se vai manter as letras maiúsculas ou especiais
                tenta -= 1

            while not found:

                combinations = itertools.product(letters, repeat=4)  #  Cria combinações de 4 caracteres
                combinations_iter = iter(combinations)  

                while True:
                    try:
                        
                        combination = next(combinations_iter)  # Gera a próxima combinação
                        senha = ''.join(combination)
                        brute = hashlib.md5(senha.encode()).hexdigest() # Gera o hash da senha

                        if brute in s: # Verifica se o hash gerado é igual ao hash da senha no arquivo

                            print(f"Senha encontrada: {''.join(combination)}")
                            fim = time.time() # Termina a contagem do tempo
                            print(f"Tempo gasto: {fim - comeco:.2f} segundos")
                            found = True
                            #print(f"Nome:{n}, tenta:{tenta}, fail:{fail}, tempo:{fim - comeco:.2f}s") # Usado para debug
                            
                            if tenta == 0: # Caso não ache nas letras minúsculas, tenta com letras maiúsculas ou especiais
                                if fail == 1:
                                    try:
                                        #print('Letras maiusculas removidas') # Usado para debug
                                        letters.clear()
                                        letters = [chr(i) for i in range(97, 123)]
                                    except:
                                        pass

                                if fail == 2:
                                    
                                    try:
                                        #print('Caractéres especiais removidos') # Usado para debug
                                        letters.clear()
                                        letters = [chr(i) for i in range(97, 123)]
                                    except:
                                        pass
                                    
                                fail = 0
                                    
                            break
                    
                    except StopIteration:  # Quando não há mais combinações
                        
                        fail += 1
                        tenta += 1

                        if fail == 1: 
                            #print("Tentando com letras maiúsculas...") # Usado para debug
                            letters.extend([chr(i) for i in range(65, 91)])  # Adiciona letras maiúsculas (A-Z)
                            tenta += 1
                        elif fail == 2:
                            #print("Tentando com caracteres especiais...") # Usado para debug
                            letters.extend([chr(i) for i in range(33, 65)])  # Caractéres especiais ('!' - '@')
                            letters.extend([chr(i) for i in range(91, 97)])  # Caractéres especiais ('[' - '`')
                            letters.extend([chr(i) for i in range(123, 127)])  # Caractéres especiais ('{' - '~')
                        break  # Reinicia loop com caractéres novos

            linha = arquivo.readline().strip()  # Vai para a próxima linha

brute_force()
print("Pressione Enter para sair...")
input()
