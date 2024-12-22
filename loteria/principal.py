from modulos import *
from outros import *
from numeros import *

while True:
    opc = menu('REBOCO Loteria Simulator v0.1',
               ['Mega-Sena',
                    'Sair do Sistema'])
    if opc == 1:                      # Mega-Sena
        precos = {'6': 5, '7':35, '8':140, '9':420, '10':1050, '11':2310,
                  '12':4620, '13':8580, '14':15015, '15':25025, '16':40040,
                  '17':61880, '18':92820, '19':135660, '20':193800}
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
        print('Você pode fazer jogos de 6 a 20 números.')
        numeros = leiaint('Quantidades de número por jogo: ', escopo=True, piso=6, teto=20)
        alvo = menu('Qual sequência você quer acertar?',
             ['Quadra - 4 números', 'Quina - 5 números', 'Sena - 6 números'])
        if alvo == 1:
            alvo = 4
        elif alvo == 2:
            alvo = 5
        elif alvo == 3:
            alvo = 6
        # Inicializa o sorteio
        linha(1, 40)
        numerosSorteados = sortear_numeros(6)
        print(f"Números sorteados: {numerosSorteados}")
        esc = input('Aperte enter para continuar...')
        # Faz os jogos
        tentativa = []
        tentativas = 0
        while True:
            tentativa = sortear_numeros(numeros)
            tentativas += 1
            print(tentativas, end='  ')
            print(tentativa)
            if acertou(numerosSorteados, tentativa, alvo):
                linha(1, 40)
                print(f'Tentativa {tentativa} acertou o jogo {numerosSorteados}.')
                print(f"Acertou os {alvo} números após {str(f'{tentativas:,}').replace(',', '.')} tentativas!")
                valor = tentativas * precos[f'{numeros}']
                print(f'Valor gasto para acertar: R$ {str(f'{valor:,}').replace(',', '.')},00.')
                break
    elif opc == 2:
        break