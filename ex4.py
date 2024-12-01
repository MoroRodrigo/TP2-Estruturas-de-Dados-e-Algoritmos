def ordenar_pilha(pilha):
    pilha_aux = []  # Pilha auxiliar para ordenação

    # Enquanto a pilha original não estiver vazia
    while pilha:
        # Remove o elemento do topo da pilha original
        temp = pilha.pop()

        # Move os elementos da pilha auxiliar de volta para a pilha original enquanto eles forem maiores que o elemento removido
        while pilha_aux and pilha_aux[-1] > temp:
            pilha.append(pilha_aux.pop())

        # Insere o elemento na pilha auxiliar
        pilha_aux.append(temp)

    # Retorna a pilha auxiliar como pilha ordenada
    return pilha_aux


# Uso
if __name__ == "__main__":
    pilha_notas = [85, 70, 92, 60, 78, 90]  # Exemplo de notas
    print("Pilha original:", pilha_notas)

    pilha_ordenada = ordenar_pilha(pilha_notas)
    print("Pilha ordenada:", pilha_ordenada)
