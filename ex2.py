def ordenar_lista(lista):
    return sorted(lista)

# Uso
if __name__ == "__main__":
    import random

    # Gera uma lista com 5 milhões de registros
    registros = [random.randint(1, 1000000) for _ in range(5000000)]
    
    print("Ordenando lista...")
    registros_ordenados = ordenar_lista(registros)
    print("Lista ordenada!")
