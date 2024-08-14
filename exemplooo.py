def criar_matriz():
    matriz = []
    print("Digite os valores para a matriz 2x2:")
    for i in range(2):
        linha = []
        for j in range(2):
            valor = float(input(f"Digite o valor para a posição ({i+1}, {j+1}): "))
            linha.append(valor)
        matriz.append(linha)
    return matriz

# Função para calcular a soma e a média dos valores da matriz
def calcular_soma_e_media(matriz):
    soma = 0
    num_elementos = 0
    for linha in matriz:
        for valor in linha:
            soma += valor
            num_elementos += 1
    media = soma / num_elementos
    return soma, media

# Função principal
def main():
    matriz = criar_matriz()
    soma, media = calcular_soma_e_media(matriz)
    
    print("\nMatriz 2x2:")
    for linha in matriz:
        print(linha)
    
    print(f"\nSoma dos valores: {soma:.2f}")
    print(f"Média dos valores: {media:.2f}")

# Executar o programa
if __name__ == "__main__":
    main()