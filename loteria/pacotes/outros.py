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

def leiaint(msg, range=False, min=0, max=10):
    """
    Coleta um número e garante que ele é do tipo 'int'.
    :param msg: Mensagem de coleta 'str'.
    (opcional)
    :param range: Pergunta se quer estabelecer um range para o número coletado.
    :param min: Mínimo do range.
    :param max: Máximo do range.
    :return: O número inteiro 'int'.
    """
    while True:
        try:
            num = int(input(f'\033[32m{msg}\033[m'))
        except ValueError:
            vermelho('ERRO! A entrada não é uma válida, tente novamente.')
        except KeyboardInterrupt:
            interrompeu()
        else:
            if range:
                if max >= num >= min:
                    return num
                else:
                    vermelho(f'Digite um valor maior entre {min} e {max}.')
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
