
def criarMatriz():
    matriz = []
    print("Digite os valores para matriz 2x2")
    for x in range(0,2):
        linha = []
        for y in range(2):
            valor = float(input(f"Digite o valor para a posição ({x+1}, {y+1}): "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

def calculoMatriz(matriz):
    soma = 0
    num_elementos = 0
    for linha in matriz:
        for valor in linha:
            soma += valor
            num_elementos += 1
    media = soma / num_elementos
    return soma, media

matriz = criarMatriz()
soma, media = calculoMatriz(matriz)
    
print("\nMatriz 2x2:")
for linha in matriz:
        print(linha)
    
print(f"\nSoma dos valores: {soma:.2f}")
print(f"Média dos valores: {media:.2f}")