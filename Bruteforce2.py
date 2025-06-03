import hashlib
import os
import itertools
import time

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))) # Define o local para abrir o arquivo
passwd_dir = os.path.join(__location__, 'usuarios.txt')
cache_dir = os.path.join(__location__, 'cache.txt')

def brute_force():

    arquivos = 0
    fail = 0
    tenta = 0
    letters = [chr(i) for i in range(97, 123)]  # Adiciona letras minúsculas (a-z)
    total = 0
    sc = None
    cache = ''
    comecototal = time.time()

    with open(passwd_dir, 'r') as arquivo: # Abre o arquivo

        linha = arquivo.readline().strip()  # Pega a primeira linha

        while linha: 

            arquivos += 1

            n, s = linha.split(',') # Separa o nome e a senha

            found = False 
            comeco = time.time() # Começa a contar o tempo
            print(f"\nProcurando senha para o usuário: {n}", end='')  # Exibe o nome do usuário

            if tenta > 0: # Usado para decidir se vai manter as letras maiúsculas ou especiais
                tenta -= 1
            
            try:
                with open (cache_dir, 'r') as cacheread:
                    sc = cacheread.readline().strip()
                    while sc:
                        if hashlib.md5(sc.encode()).hexdigest() in s:
                            print(f"\rUsuário:{n}", " "*23, f"\nSenha encontrada no cache: {sc}\n", end='')
                            found = True
                            fim = time.time()
                            print(f"Tempo gasto: {fim-comeco:.2f} segundos\nMédia de tempo gasto atual: {total/arquivos:.2f} segundos")
                            break
                        sc = cacheread.readline().strip()
            except:
                pass

            while not found:

                combinations = itertools.product(letters, repeat=4)  #  Cria combinações de 4 caracteres
                combinations_iter = iter(combinations)  

                while True:
                    try:
                        
                        combination = next(combinations_iter)  # Gera a próxima combinação
                        senha = ''.join(combination)
                        brute = hashlib.md5(senha.encode()).hexdigest() # Gera o hash da senha

                        if brute in s: # Verifica se o hash gerado é igual ao hash da senha no arquivo

                            print(f"\rUsuário:{n}", " "*23, f"\nSenha encontrada: {''.join(combination)}\n", end='')
                            fim = time.time() # Termina a contagem do tempo
                            total += fim-comeco
                            print(f"Tempo gasto: {fim-comeco:.2f} segundos\nMédia de tempo gasto atual: {total/arquivos:.2f} segundos")
                            found = True
                            with open(cache_dir, 'a') as savecache:
                                savecache.write(f"{senha}\n")
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

    fimtotal = time.time()
    totalexec = fimtotal - comecototal
    print(f"\nTempo total: {totalexec:.2f} segundos\nTempo médio final: {totalexec/arquivos:.2f} segundos\nSenhas encontradas: {arquivos}")

brute_force()
print("\nPressione Enter para sair...")
input()
