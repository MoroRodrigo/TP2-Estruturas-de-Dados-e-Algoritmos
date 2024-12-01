def ordenar_lista(lista):
    n = len(lista)
    
    # Loop principal que percorre toda a lista
    for i in range(n):
        # Compara pares de elementos adjacentes
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:  # Troca se estiver fora de ordem
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    
    return lista


# Uso
if __name__ == "__main__":
    lista_numeros = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", lista_numeros)
    lista_ordenada = ordenar_lista(lista_numeros)
    print("Lista ordenada:", lista_ordenada)
