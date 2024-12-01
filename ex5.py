def tarefa_no_topo(pilha_de_tarefas):
    if not pilha_de_tarefas:
        return "A pilha de tarefas está vazia."
    return pilha_de_tarefas[-1]


# Uso
if __name__ == "__main__":
    # Exemplo de pilha de tarefas
    pilha_tarefas = ["Tarefa 1: Escrever relatório", 
                     "Tarefa 2: Reunião com o time", 
                     "Tarefa 3: Finalizar código"]

    print("Pilha de tarefas:", pilha_tarefas)
    proxima_tarefa = tarefa_no_topo(pilha_tarefas)
    print("Próxima tarefa a ser concluída:", proxima_tarefa)
