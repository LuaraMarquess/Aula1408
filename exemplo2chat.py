def obter_escalacao():
    """Recebe e retorna a escalação inicial dos jogadores em uma lista de tuplas (nome, número)."""
    escalacao = []
    for _ in range(3): # for _in range(11) estou usando até o 3 para testar
        #nome = input("Nome do jogador: ").strip() #strip remove espaço em branco
        nome = input("Digite o nome do jogador: ")
        numero = input("Número da camisa: ")
        escalacao.append((nome, numero))
    return escalacao

def imprimir_escalacao(escalacao):
    """Imprime a lista atualizada de jogadores."""
    print("\nEscalação atual:")
    for i, (nome, numero) in enumerate(escalacao, 1):
        print(f"{i}. Número: {numero} - Nome: {nome}")

def substituir_jogadores(escalação):
    """Permite ao técnico substituir até 3 jogadores na lista."""
    for _ in range(3):
        numero_antigo = input("\nNúmero da camisa a ser substituído: ").strip()
        encontrado = False
        
        for i, (nome, numero) in enumerate(escalação):
            if numero == numero_antigo:
                novo_nome = input("Nome do novo jogador: ").strip()
                novo_numero = input("Número da nova camisa: ").strip()
                escalação[i] = (novo_nome, novo_numero)
                encontrado = True
                break
        
        if not encontrado:
            print("Número de camisa não encontrado.")
    
    return escalação

def main():
    """Função principal do programa."""
    print("Digite a escalação dos 11 jogadores:")
    escalação = obter_escalacao()
    imprimir_escalacao(escalação)
    
    print("\nDurante o intervalo, você pode substituir até 3 jogadores.")
    escalação = substituir_jogadores(escalação)
    imprimir_escalacao(escalação)

if __name__ == "__main__":
    main()