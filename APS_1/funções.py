def matirz(fileira, cadeira):
    aviao = []
    cadeiras = []
    for a in range(cadeira):
        cadeiras.append(0)
    for b in range(fileira):
        aviao.append(cadeiras[:])
    cadeiras.clear()
    return aviao


def impressão(matriz):
    for c in matriz:
        print(c)


def ocupação(fileira, assento, matriz):
    matriz[fileira-1][assento-1] = 1


def exclusão(fileira, assento, matriz):
    matriz[fileira-1][assento-1] = 0


def cadastro(nome, cpf, dic):
    dic[cpf] = nome
    return dic


def consultacadastro(cpf, dic):
    if cpf in dic:

        print(f'O CPF {cpf} está registrado no nome de {dic.get(cpf)}')
    else:

        print('Usuário não registrado!')


def reserva(cpf, assento, dic):
    dic[cpf] = assento
    return dic


def cancelamentodereserva(cpf, dic):
    del dic[cpf]

def listar_assento_disponiveis(aviao):
    disponiveis = []
    for i in range(len(aviao)):
        for j in range(len(aviao[i])):
            if aviao[i][j] == False:
                disponiveis.append(j+1)
        print(f'Fila {i+1}: {disponiveis}')
        disponiveis = []

