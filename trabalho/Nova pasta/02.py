import hashlib
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


print('-------Sistema de Cadastro e Auntenticação')

while True:

    print('escolha uma opcção :  \n 1- Cadastrar o usuario \n 2- Auntenticar o Usuario \n 3- Sair')
    opcao = int(input('>   '))

    if opcao == 1:   #cadastrar
        with open('cadastros.txt' , 'a') as cadastro:

            print('digite o nome de usuario (deve ter 4 letras)')
            user = input('>    ')
            if len(user) != 4:
                print('o nome de usuario deve ter 4 letras')
            else:
                cadastro.write(user) #falta fazer registrar os nomes um abaixo do outro


            print('nome de usuario salvo com sucesso , agora digite a senha (deve ter 4 caracteres)')
            psw = input('>   ')
            if len(psw) != 4:
                print('a senha deve der 4 caracteres')
            else:
                code_psw = hashlib.md5(psw.encode())
                code_psw = code_psw.hexdigest()
                cadastro.write(code_psw)