import hashlib
import os
import itertools
import time

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
passwd_dir = os.path.join(__location__, 'usuarios.txt')



def brute_force():
    letters = [chr(i) for i in range(97, 123)] # ASCII lowercase letters (a-z)
    letters.extend([chr(i) for i in range(65, 91)]) # ASCII uppercase letters (A-Z)
    #letters.extend([chr(i) for i in range(33, 65)]) # ASCII characters from '!' (32) to '@' (64)
    letters.extend([chr(i) for i in range(91, 97)])  # ASCII characters from '[' (91) to '`' (96)
    #letters.extend([chr(i) for i in range(123, 127)]) # ASCII characters from '{' (123) to '~' (126)
    with open (passwd_dir, 'r') as arquivo:
        for linha in arquivo:
            formatline = linha.strip()
            n, s = formatline.split(',')
            print(formatline)
            found = False
            comeco = time.time()
            for combination in itertools.product(letters, repeat=4):
                print(f"Tentando: {''.join(combination)}, {n}, {found}")
                senha = ''.join(combination)
                brute = hashlib.md5(senha.encode()).hexdigest()   
                if brute in s:
                    print(f"Senha encontrada: {''.join(combination)}")
                    fim = time.time()
                    print(f"Tempo gasto: {fim - comeco:.2f} segundos")
                    found = True
                    break

brute_force()
