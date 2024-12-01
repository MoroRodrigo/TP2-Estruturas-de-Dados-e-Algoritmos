from collections import deque

class FilaAtendimento:
    def __init__(self):
        """
        Inicializa a fila de atendimento como uma fila vazia.
        """
        self.fila = deque()

    def adicionar_cliente(self, nome):
        """
        Adiciona um cliente ao final da fila.
        """
        self.fila.append(nome)
        print(f"Cliente {nome} adicionado à fila.")

    def atender_cliente(self):
        """
        Remove o cliente do início da fila e exibe o nome do cliente atendido.
        """
        if self.fila:
            cliente_atendido = self.fila.popleft()
            print(f"Cliente {cliente_atendido} atendido.")
        else:
            print("A fila está vazia. Nenhum cliente para atender.")

    def tamanho_fila(self):
        """
        Retorna o número de clientes restantes na fila.
        """
        return len(self.fila)


# Uso
if __name__ == "__main__":
    fila_atendimento = FilaAtendimento()
    
    # Adicionando clientes
    fila_atendimento.adicionar_cliente("João")
    fila_atendimento.adicionar_cliente("Maria")
    fila_atendimento.adicionar_cliente("Pedro")
    
    # Atendendo clientes
    fila_atendimento.atender_cliente()
    
    # Verificando tamanho da fila
    print("Clientes restantes na fila:", fila_atendimento.tamanho_fila())
    
    # Atendendo mais clientes
    fila_atendimento.atender_cliente()
    fila_atendimento.atender_cliente()
    
    # Verificando novamente o tamanho da fila
    print("Clientes restantes na fila:", fila_atendimento.tamanho_fila())
