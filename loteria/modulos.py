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
        esc = leiaint('Sua opção: ', escopo=True, piso=1, teto=len(opc), flag=-1, foramsg='Opção fora da lista.')
        return esc

def simularunico(precos, cartela, aposta, sequencia, sorteio):
    """
    Coleta os parãmetros de aposta de um jogador e simula apostas sequenciais até que uma acerte a sequencia alvo
    determinada.
    :param precos: 'dict' com o preço dos jogos, index == QTD de números, valor == preço da aposta equivalente
    :param cartela: 'dict' QTD de núemros da cartela, 'piso' == valor mínimo, 'teto' == valor máximo
    :param aposta: 'dict' QTD de números por aposta. 'piso' == valor mínimo, 'teto' == valor máximo
    :param sequencia: dict' QTD de números por aposta. 'piso' == valor mínimo, 'teto' == valor máximo
    :param sorteio: 'dict' QTD de acertos possíveis, 'piso' == valor mínimo, 'teto' == valor máximo
                    Usar 'txt' caso as sequências tiverem nomes e quiser especificá-las.
    :return: Nada, mostra tudo na tela sozinha.
    """
    titulo('Quer simular jogos de quantos números?')
    print(f'Você pode fazer jogos de {aposta['piso']} a {aposta['teto']} números.')
    numeros = leiaint('Quantidades de número por jogo: ', escopo=True, piso=aposta['piso'], teto=aposta['teto'], flag=0)
    if numeros == 0:
        return

    # Coleta a sequencia que a simulação deverá acertar antes de parar
    titulo('Qual sequência você quer acertar?')
    if sequencia['txt'] == '':
        print(f'Você pode tentar acertar de {sequencia['piso']} a {sequencia['teto']} números.')
    else:
        print(sequencia['txt'])
    alvo = leiaint('Sequência: ', escopo=True, piso=sequencia['piso'], teto=sequencia['teto'], flag=0)
    if alvo == 0:
        return

    # Sorteia os números
    linha(1, 40)
    numeros_sorteados = sortear_numeros(sorteio, cartela['piso'], cartela['teto'])
    print(f"Números sorteados: {numeros_sorteados}")
    try:
        input('Aperte enter para continuar...')
    except KeyboardInterrupt:
        interrompeu()
        return

    # Faz os jogos e testa se acertou
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
