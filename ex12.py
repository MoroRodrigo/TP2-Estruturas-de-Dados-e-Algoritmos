class TabelaHash:
    def __init__(self, tamanho):
        """
        Inicializa a tabela hash com o tamanho especificado.
        """
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]  # Cria a tabela com listas vazias

    def _hash(self, chave):
        """
        Função hash simples.
        """
        return hash(chave) % self.tamanho

    def inserir(self, chave, valor):
        """
        Insere uma chave e seu valor na tabela hash.
        """
        indice = self._hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:  # Se a chave já existe atualiza o valor
                item[1] = valor
                return
        self.tabela[indice].append([chave, valor])  # Se não existir a chave adiciona o novo par chave-valor
        print(f"Chave '{chave}' com valor '{valor}' inserida.")

    def buscar(self, chave):
        """
        Busca o valor associado a uma chave.
        """
        indice = self._hash(chave)
        for item in self.tabela[indice]:
            if item[0] == chave:
                return item[1]
        return "Não encontrado"

    def remover(self, chave):
        """
        Remove uma chave e seu valor da tabela hash.
        """
        indice = self._hash(chave)
        for i, item in enumerate(self.tabela[indice]):
            if item[0] == chave:
                del self.tabela[indice][i]
                print(f"Chave '{chave}' removida.")
                return
        print(f"Chave '{chave}' não encontrada na tabela.")

# Uso
if __name__ == "__main__":
    tabela_hash = TabelaHash(10)  # Tabela com 10 posições

    # Inserindo elementos
    tabela_hash.inserir("nome", "João")
    tabela_hash.inserir("idade", 30)
    tabela_hash.inserir("cidade", "São Paulo")

    # Buscando elementos
    print("Busca por 'nome':", tabela_hash.buscar("nome"))
    print("Busca por 'idade':", tabela_hash.buscar("idade"))
    print("Busca por 'cidade':", tabela_hash.buscar("cidade"))
    print("Busca por 'email':", tabela_hash.buscar("email"))  # Não existe

    # Removendo elementos
    tabela_hash.remover("idade")
    print("Busca por 'idade' após remoção:", tabela_hash.buscar("idade"))

    # Tentando remover um item que não existe
    tabela_hash.remover("email")
