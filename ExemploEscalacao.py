def obter_escalacao():
    """Recebe e retorna a escalação inicial dos jogadores em duas listas separadas: nomes e números."""
    nomes = []
    numeros = []
    
    for _ in range(2):
        nome = input("Nome do jogador: ")
        numero = input("Número da camisa: ")
        nomes.append(nome) 
        numeros.append(numero)
    
    return nomes, numeros

def imprimir_escalacao(nomes, numeros):
    """Imprime a lista atualizada de jogadores usando duas listas separadas."""
    print("\nEscalação atual:")
    for i in range(len(nomes)):
        print(f"{i + 1}. Número: {numeros[i]} - Nome: {nomes[i]}")

def substituir_jogadores(nomes, numeros):
    """Permite ao técnico substituir até 3 jogadores na lista usando duas listas separadas."""
    for _ in range(3):
        numero_antigo = input("\nNúmero da camisa a ser substituído: ")
        if numero_antigo in numeros:
            index = numeros.index(numero_antigo)
            novo_nome = input("Nome do novo jogador: ")
            novo_numero = input("Número da nova camisa: ")
            nomes[index] = novo_nome
            numeros[index] = novo_numero
        else:
            print("Número de camisa não encontrado.")
    
    return nomes, numeros

#def main():
    """Função principal do programa."""
print("Digite a escalação dos 11 jogadores:")
nomes, numeros = obter_escalacao()
imprimir_escalacao(nomes, numeros)
    
print("\nDurante o intervalo, você pode substituir até 3 jogadores.")
nomes, numeros = substituir_jogadores(nomes, numeros)
imprimir_escalacao(nomes, numeros)

#if __name__ == "__main__":
 #   main()