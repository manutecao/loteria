def linha(tipo=1,tam=0):
    """ Mostra uma linha na tela:
    ------------------------------
    :param tipo: 1 - linha simples (-----------), 2 - linha e igual (-=-=-=-=-=-=-)
    :param tam: 'int' tamanho da lista, obs: o 'tam' é multiplicado pelo tipo (1 ou 2)
    :return:
    """
    if tipo == 1:
        print('-' * tam)
    elif tipo == 2:
        print('-' * tam)

def titulo(msg):
    """ Mostra isso na tela:
    ---------------
        Exemplo
    ---------------
    :param msg: Mensagem a ser mostrada 'str'.
    :return:
    """
    linha(1, (len(msg)+4))
    print(msg.center(len(msg)+4))
    linha(1, (len(msg)+4))

def leiaint(msg, flag=0, escopo=False, piso=0, teto=10):
    """
    Coleta um número e garante que ele é do tipo 'int'.
    :param msg: Mensagem de coleta 'str'.
    :param flag: 'int' que será retornado em caso de
    'KeyboardInterruptError'
    (Opcional:)
        :param escopo: padrão 'False', determina escopo do número a ser coletado.
        :param piso: Limite mínimo do escopo 'int'.
        :param teto: Limite máximo do escopo 'int'.
    :return: O número inteiro 'int' que foi coletado
    """
    while True:
        try:
            num = int(input(f'\033[32m{msg}\033[m'))
        except ValueError:
            vermelho('ERRO! A entrada não é uma válida, tente novamente.')
        except KeyboardInterrupt:
            interrompeu()
            return flag
        else:
            if escopo:
                if teto >= num >= piso:
                    return num
                else:
                    print(f'Digite um número entra {piso} e {teto}.')
            else:
                return num

def vermelho(msg):
    """
    Mostra na tela uma mensagem na tela com a cor da fonte em vermelho.
    :param msg: Mensagem a ser mostrada.
    :return:
    """
    print(f'\033[31m{msg}\033[m')

def interrompeu():
    """
    Mostra na tela uma mensagem alertando que o usuário interrompeu a operação.
    :return:
    """
    print('O usuário interrompeu a operação.')
