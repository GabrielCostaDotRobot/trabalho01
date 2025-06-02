import hashlib
import itertools
import string
import time

# Função para quebrar um hash MD5 de senha de tamanho variável
def quebrar_md5(hash_alvo, tamanho_min=4, tamanho_max=8):
    chars = string.ascii_lowercase + string.digits  # Letras minúsculas e números
    
    for tamanho in range(tamanho_min, tamanho_max + 1):
        print(f'Tentando senhas de {tamanho} caracteres...')
        for tentativa in itertools.product(chars, repeat=tamanho):
            senha = ''.join(tentativa)
            hash_senha = hashlib.md5(senha.encode()).hexdigest()
            if hash_senha == hash_alvo:
                return senha
    return None

# Ler os hashes do arquivo
with open('cadastros.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

resultados = []

for linha in linhas: 
    user, hash_senha = linha.strip().split()
    print(f'\nQuebrando senha do usuário: {user}')
    
    inicio = time.time()
    senha_encontrada = quebrar_md5(hash_senha, tamanho_min=4, tamanho_max=8)
    fim = time.time()
    
    tempo = fim - inicio
    
    if senha_encontrada:
        print(f'✅ Senha encontrada: {senha_encontrada} em {tempo:.2f} segundos')
    else:
        print('❌ Senha não encontrada')
    
    resultados.append([user, senha_encontrada, f'{tempo:.2f} segundos'])

# Exibir os resultados em forma de tabela
print('\nTabela de Resultados:')
print('Usuário | Senha | Tempo')
for r in resultados:
    print(f'{r[0]}       | {r[1]}   | {r[2]}')
