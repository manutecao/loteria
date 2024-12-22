from outros import *
from time import sleep

def menu(txt, opc):
    """ Mostra um menu na tela e coleta a opção escolhida:
    ------------------------------
            MENU PRINCIPAL
    ------------------------------
     1 - Ver pessoas cadastradas
     2 - Cadastrar nova Pessoa
     3 - Sair do Sistema
    ------------------------------
    Sua opção: 1
    ------------------------------
    :param txt: Título do menu 'str'
    :param opc: Lista com as opções 'str' a serem disponibilizadas no menu.
    :return: A opção escolhida 'int'.
    """
    if opc is None:
        opc = list()
    titulo(txt)
    for op in range(0, len(opc)):
        print(f' {op + 1} - \033[34m{opc[op]:<23}\033[m')
    linha(1, 30)
    while True:
        esc = leiaint('Sua opção: ')
        if esc < 0 or esc > len(opc):
            vermelho(f'\'{esc}\' não é uma opção do menu.')
        else:
            return esc
