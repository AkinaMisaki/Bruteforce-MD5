import hashlib
import os
import itertools
import time

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
passwd_dir = os.path.join(__location__, 'usuarios.txt')

def brute_force():
    fail = 0
    tenta = 0
    letters = [chr(i) for i in range(97, 123)]  # ASCII lowercase (a-z)

    with open(passwd_dir, 'r') as arquivo:
        linha = arquivo.readline().strip()  # Read first line

        while linha:  # Process each password entry
            n, s = linha.split(',')
            #print(linha)
            found = False
            comeco = time.time()
            if tenta > 0:
                tenta -= 1

            while not found:
                combinations = itertools.product(letters, repeat=4)  # Create iterator
                combinations_iter = iter(combinations)  # Explicitly make it an iterator

                while True:
                    try:
                        
                        combination = next(combinations_iter)  # Get next combination
                        senha = ''.join(combination)
                        brute = hashlib.md5(senha.encode()).hexdigest()

                        if brute in s:
                            #print(f"Senha encontrada: {''.join(combination)}")
                            fim = time.time()
                            #print(f"Tempo gasto: {fim - comeco:.2f} segundos")
                            found = True
                            print(f"Nome:{n}, tenta:{tenta}, fail:{fail}, tempo:{fim - comeco:.2f}s")
                            if tenta == 0:
                                if fail == 1:
                                    try:
                                        #print('Letras maiusculas removidas')
                                        letters.clear()
                                        letters = [chr(i) for i in range(97, 123)]
                                    except:
                                        pass

                                if fail == 2:
                                    
                                    try:
                                        #print('Caractéres especiais removidos')
                                        letters.clear()
                                        letters = [chr(i) for i in range(97, 123)]
                                    except:
                                        pass
                                    
                                fail = 0
                                    
                            break
                    
                    except StopIteration:  # Iterator is exhausted
                        
                        fail += 1
                        tenta += 1

                        if fail == 1:
                            #print("Tentando com letras maiúsculas...")
                            letters.extend([chr(i) for i in range(65, 91)])  # Add uppercase letters
                            tenta += 1
                        elif fail == 2:
                            #print("Tentando com caracteres especiais...")
                            letters.extend([chr(i) for i in range(33, 65)])  # Special characters ('!' - '@')
                            letters.extend([chr(i) for i in range(91, 97)])  # Special characters ('[' - '`')
                            letters.extend([chr(i) for i in range(123, 127)])  # Special characters ('{' - '~')
                        #print(letters)
                        break  # Restart loop with new letters

            linha = arquivo.readline().strip()  # Read next line

brute_force()
print("Pressione Enter para sair...")
input()
