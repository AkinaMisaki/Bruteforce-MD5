import hashlib
import os
import itertools
import time

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
passwd_dir = os.path.join(__location__, 'usuarios.txt')


def brute_force():
    comeco = time.time()
    letters = [chr(i) for i in range(97, 123)] 
    for combination in itertools.product(letters, repeat=4):
        print(f"Tentando: {''.join(combination)}")
        senha = ''.join(combination)
        brute = hashlib.md5(senha.encode()).hexdigest()
        with open (passwd_dir, 'r') as f:
            for x in f:
                n, s = x.strip().split(',')
                if brute in s:
                    print(f"Senha encontrada: {''.join(combination)}")
                    fim = time.time()
                    print(f"Tempo gasto: {fim - comeco:.2f} segundos")
                    return


brute_force()