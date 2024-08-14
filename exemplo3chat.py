def exibir_lista(lista):
    """Função para exibir a lista de afazeres"""
    print("\nLista de Afazeres:")
    for i, tarefa in enumerate(lista, 1):
        print(f"{i}. {tarefa}")

def adicionar_tarefa(lista):
    """Função para adicionar uma nova tarefa à lista"""
    if len(lista) >= 5:
        print("A lista já está completa. Você deve remover uma tarefa antes de adicionar uma nova.")
        return
    
    nova_tarefa = input("Digite a nova tarefa: ").strip()
    lista.append(nova_tarefa)

def main():
    """Função principal do programa"""
    tarefas = []
    
    # Criação da lista de afazeres com 5 tarefas
    print("Digite 5 tarefas para a lista de afazeres:")
    for _ in range(5):
        tarefa = input(f"Tarefa {_ + 1}: ").strip()
        tarefas.append(tarefa)
    
    exibir_lista(tarefas)
    
    # Pergunta se a primeira tarefa foi executada
    resposta = input("\nA primeira tarefa foi executada? (sim/não): ").strip().lower()
    
    if resposta == 'sim':
        if tarefas:
            # Remove a primeira tarefa
            tarefas.pop(0)
            print("\nPrimeira tarefa removida.")
            
            # Exibe a lista atualizada
            exibir_lista(tarefas)
            
            # Adiciona uma nova tarefa
            adicionar_tarefa(tarefas)
            
            # Exibe a lista final após a adição
            print("\nLista de Afazeres Atualizada:")
            exibir_lista(tarefas)
        else:
            print("A lista está vazia, não há tarefas para remover.")
    else:
        print("Nenhuma tarefa foi removida.")
        exibir_lista(tarefas)

if __name__ == "__main__":
    main()