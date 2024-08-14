GABARITO = ['B', 'C', 'A', 'E', 'D']

def verificar_acertos(respostas):
    """Função para verificar a quantidade de acertos"""
    acertos = 0
    for i in range(len(GABARITO)):
        if respostas[i] == GABARITO[i]:
            acertos += 1
    return acertos


print("Digite suas respostas para as 5 questões (uma por vez):")
respostas_usuario = []
    
for i in range(0,5):
        resposta = input(f"Questão {i + 1}: ").strip().upper() #Upper colocando em maiusculo
        while resposta not in ['A', 'B', 'C', 'D', 'E']:
            print("Resposta inválida. Por favor, insira uma das opções: A, B, C, D ou E.")
            resposta = input(f"Questão {i + 1}: ").strip().upper()
        respostas_usuario.append(resposta)
    
    # Verifica a quantidade de acertos
acertos = verificar_acertos(respostas_usuario)
print(f"Você acertou {acertos} de 5 questões.")

