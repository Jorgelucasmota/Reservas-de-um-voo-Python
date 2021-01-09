from APS_1 import funções

fileiras = 20
cadeiras = 4
aviao = funções.matirz(fileiras, cadeiras)
cadastros = {}
reservas = {}
cancelados = []

while True:
    print('')
    print('=-=' * 20)
    print(
        '1-Cadastro de Cliente (Nome, CPF)\n2-Consulta de Clientes (Pelo CPF)\n3-Reserva de Assento (Fileira, Assento e CPF do Cliente)\n4-Cancelamento de Reserva de Assento (Pelo CPF do Cliente)')
    print(
        '5-Relatório de Reservas (Assento + Cliente que reservou)\n6-Relatório de Assentos Livres\n7-Relatório de Cancelamento de Reservas de Assento)')
    print('0-Sair')
    print('=-=' * 20)
    opcao = int(input('OPÇÃO:'))
    print('')
    if opcao == 0:
        print('Obrigado!')
        break
    if opcao == 1:
        print('=-=' * 20)
        nome = input('Informe o seu nome: ')
        cpf = input('Informe o seu CPF ( sem pontos e traço ): ')
        while cpf in cadastros:
            print('Usuário ja registrado!')
            nome = input('Informe o seu nome: ')
            cpf = input('Informe o seu CPF ( sem pontos e traço ): ')
        funções.cadastro(nome, cpf, cadastros)
    if opcao == 2:
        print('=-=' * 20)
        cpf1 = input('Informe o CPF do cliente: ')  
        funções.consultacadastro(cpf1, cadastros)
    if opcao == 3:
        print('=-=' * 20)
        cpf2 = input('Informe o CPF do cliente:')
        while cpf2 not in cadastros:
            print('Cliente nao cadastrado.')
            cpf2 = input('Informe o CPF do cliente:')
        assento = input('Informe a fileira e o assento (ex.: 1 1): ')
        local = assento.split(' ')
        local = [int(i) for i in local]
        funções.reserva(cpf2, assento, reservas)
        funções.ocupação(local[0], local[1], aviao)
    if opcao == 4:
        print('=-=' * 20)
        cpf3 = input('Informe o CPF do cliente: ')
        while cpf3 not in cadastros:
            print('Cliente nao cadastrado.')
        print('Acento do clinte cancelado!')
        apagar = reservas.get(cpf3)
        cancelados.append(apagar)
        separa = apagar.split(' ')
        separa = [int(y) for y in separa]
        funções.exclusão(separa[0], separa[1], aviao)
        funções.cancelamentodereserva(cpf3, reservas)
    if opcao == 5:
        print('=-=' * 20)
        for key in reservas.keys() and cadastros.keys():
            print(f'{cadastros.get(key)}: {reservas.get(key)}')
    if opcao == 6:
        print('=-=' * 20)
        funções.listar_assento_disponiveis(aviao)
    if opcao == 7:
        for q in range(len(cancelados)):
            print(f'O assento {cancelados[q]} foi cancelado.')
