def encontrar_duplicados_bruto(lista):
    duplicados = []
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j] and lista[i] not in duplicados:
                duplicados.append(lista[i])
    return duplicados

# Uso
if __name__ == "__main__":
    lista_teste = [1, 2, 3, 2, 4, 5, 1, 6]
    print("Duplicados (força bruta):", encontrar_duplicados_bruto(lista_teste))
