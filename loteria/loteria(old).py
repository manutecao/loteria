import random

# Sorteia os 6 números únicos entre 1 e 60
def sortear_numeros():
    return sorted(random.sample(range(1, 61), 6))

# Verifica se a lista sorteada é duplicada
def duplicada():
    if tentativa not in jogos:
        jogos.append(tentativa[:])
        return True
    else:
        return False

# Verifica se duas listas são iguais
def acertou():
    return numeros_sorteados == tentativa

# Inicializa o sorteio
numeros_sorteados = sortear_numeros()
print(f"Números sorteados: {numeros_sorteados}")
esc = input('Aperte enter para continuar...')

jogos = []
tentativa = []
tentativas = 0
while True:
    tentativa = sortear_numeros()
    if duplicada():
        tentativas += 1
        print(tentativas, end='  ')
        print(tentativa)
        if acertou(numeros_sorteados, tentativa):
         print(f"Acertou os números após {tentativas} tentativas!")
         break
