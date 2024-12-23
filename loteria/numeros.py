from random import sample

# Sorteia os 6 números únicos entre 1 e 60
def sortear_numeros(qtd, piso, teto):
    return sorted(sample(range(piso, teto+1), qtd))

# Verifica se duas listas são iguais
def acertou(num_sorteados, tentativa, atingir=0):
    cont = 0
    for num in tentativa:
        if num in num_sorteados:
            cont += 1
    if cont == atingir:
        return True
