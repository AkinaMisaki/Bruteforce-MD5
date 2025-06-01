import hashlib
import os
import itertools
import time

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
passwd_dir = os.path.join(__location__, 'usuarios.txt')



def brute_force():
    fail = 0
    letters = [chr(i) for i in range(97, 123)] # ASCII de letras minúsculas (a-z)
    with open (passwd_dir, 'r') as arquivo:
        for linha in arquivo:
            formatline = linha.strip()
            n, s = formatline.split(',')
            print(formatline)
            found = False
            comeco = time.time()
            combinations = itertools.product(letters, repeat=4)
            while True:
                try:
                    combination = next(combinations)
                    #if n == 'spec':
                    #    print(f"Tentando: {''.join(combination)}, {n}, {found}")
                    senha = ''.join(combination)
                    brute = hashlib.md5(senha.encode()).hexdigest()
                    
                    if brute in s:
                        print(f"Senha encontrada: {''.join(combination)}")
                        fim = time.time()
                        print(f"Tempo gasto: {fim - comeco:.2f} segundos")
                        found = 'Encontrado'
                        break
                except StopIteration:
                    print("Tentativas esgotadas.")
                    fail += 1
                    print(fail)
                    if fail == 1:
                        letters.extend([chr(i) for i in range(65, 91)]) # ASCII de letras maiúsculas (A-Z)
                    elif fail == 2:
                        print("Tentando com caracteres especiais...")
                        letters.extend([chr(i) for i in range(33, 65)]) # ASCII de símbolos especiais ('!' (32) até '@' (64))
                        letters.extend([chr(i) for i in range(91, 97)])  # ASCII de símbolos especiais ('[' (91) até '`' (96))
                        letters.extend([chr(i) for i in range(123, 127)]) # ASCII de símbolos especiais ('{' (123) até '~' (126))
                    break
                    


brute_force()
