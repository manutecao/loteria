from modulos import *

while True:
    opc = menu('REBOCO Loteria Simulator v0.1',
               ['Mega-Sena',
                    'Lotofácil',
                    'Sair do Sistema'])
    if opc == 1:                      # Mega-Sena
        precos = {'6': 5, '7':35, '8':140, '9':420, '10':1050, '11':2310,
                  '12':4620, '13':8580, '14':15015, '15':25025, '16':40040,
                  '17':61880, '18':92820, '19':135660, '20':193800}
        cartela = {'piso': 1, 'teto': 60}
        aposta = {'piso':6, 'teto':20}
        sequencia = {'txt':'Quadra - 4 números, Quina - 5 números, Sena - 6 números', 'piso':4, 'teto': 6}
        sorteio = 6
        simular(precos, cartela, aposta, sequencia, sorteio)
    elif opc == 2:
        precos = {'15': 3, '16': 48, '17': 408, '18': 2448, '19': 11628, '20': 46512}
        cartela = {'piso':1, 'teto':25}
        aposta = {'piso': 15, 'teto': 20}
        sequencia = {'txt':'', 'piso':11, 'teto':15}
        sorteio = 15
        simular(precos, cartela, aposta, sequencia, sorteio)
    elif opc == 3:
        break