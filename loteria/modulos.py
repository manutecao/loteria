from outros import *
from numeros import *

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

def simular(precos, cartela, aposta, sequencia, sorteio):
    """numQtd = menu('Quer simular jogos de quantos números?',
                         ['6 números','7 números', '8 números', 'Outro número'])
           if numQtd == 1:
               numeros = 6
           elif numQtd == 2:
               numeros = 7
           elif numQtd == 3:
               numeros = 8
           elif numQtd == 4:
               numeros = leiaint('Escolha outro número: ', True,9, 20)"""

    titulo('Quer simular jogos de quantos números?')
    print(f'Você pode fazer jogos de {aposta['piso']} a {aposta['teto']} números.')
    numeros = leiaint('Quantidades de número por jogo: ', escopo=True, piso=aposta['piso'], teto=aposta['teto'])

    """alvo = menu('Qual sequência você quer acertar?',
         ['Quadra - 4 números', 'Quina - 5 números', 'Sena - 6 números'])
    if alvo == 1:
        alvo = 4
    elif alvo == 2:
        alvo = 5
    elif alvo == 3:
        alvo = 6"""

    titulo('Qual sequência você quer acertar?')
    if sequencia['txt'] == '':
        print(f'Você pode tentar acertar de {sequencia['piso']} a {sequencia['teto']} números.')
    else:
        print(sequencia['txt'])
    alvo = leiaint('Sequência: ', escopo=True, piso=sequencia['piso'], teto=sequencia['teto'])

    # Inicializa o sorteio
    linha(1, 40)
    numeros_sorteados = sortear_numeros(sorteio, cartela['piso'], cartela['teto'])
    print(f"Números sorteados: {numeros_sorteados}")
    input('Aperte enter para continuar...')
    # Faz os jogos
    #tentativa = []
    tentativas = 0
    while True:
        tentativa = sortear_numeros(numeros, cartela['piso'], cartela['teto'])
        tentativas += 1
        print(tentativas, end='  ')
        print(tentativa)
        if acertou(numeros_sorteados, tentativa, alvo):
            linha(1, 40)
            print(f'Tentativa {tentativa} acertou o jogo {numeros_sorteados}.')
            print(f"Acertou os {alvo} números após {str(f'{tentativas:,}').replace(',', '.')} tentativas!")
            valor = tentativas * precos[f'{numeros}']
            print(f'Valor gasto para acertar: R$ {str(f'{valor:,}').replace(',', '.')},00.')
            break
