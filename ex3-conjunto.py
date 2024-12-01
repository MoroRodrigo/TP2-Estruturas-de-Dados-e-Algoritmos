def encontrar_duplicados_set(lista):
    vistos = set()
    duplicados = set()
    for numero in lista:
        if numero in vistos:
            duplicados.add(numero)
        else:
            vistos.add(numero)
    return list(duplicados)

# Uso
if __name__ == "__main__":
    lista_teste = [1, 2, 3, 2, 4, 5, 1, 6]
    print("Duplicados (com set):", encontrar_duplicados_set(lista_teste))
