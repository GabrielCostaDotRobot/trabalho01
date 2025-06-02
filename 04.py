import hashlib     #importa a hashlib   

print('-------Sistema de Cadastro e Auntenticação')       

while True:

    print('escolha uma opcção :  \n 1- Cadastrar o usuario \n 2- Auntenticar o Usuario \n 3- Sair')
    opcao = int(input('>   '))

    if opcao == 1:   # Cadastrar
        with open('cadastros.txt', 'a') as cadastro:
            print('Digite o nome de usuário ')
            user = input('> ')
            print('Agora digite a senha (deve ter no minimo 6 caracteres)')
            psw = input('> ')
            if len(psw) < 6:
                print(' A senha deve ter no minimo 6 caracteres')
            else:
                code_psw = hashlib.md5(psw.encode()).hexdigest()
                cadastro.write(f'{user} {code_psw}\n')
                print('Usuário cadastrado com sucesso')




    elif opcao == 2:
        autenticado = False

        print('digite o nome do usuario :')
        aut_user = input('>     ')
        print('digite sua senha')
        aut_psw = input('>      ')

        #gera o hash da senha
        aut_psw_hash = hashlib.md5(aut_psw.encode()).hexdigest()

        with open('cadastros.txt' , 'r') as cadastro:
            for i in cadastro:
                user , senha_hash = i.strip().split()

                if aut_user == user and aut_psw_hash == senha_hash:
                    autenticado = True

        if autenticado:
            print('Usuario foi autenticado com sucesso!')
        else:
            print('Usuario ou senha incorretos.')
            

    elif opcao ==3:
        print('saindo.......')
        break