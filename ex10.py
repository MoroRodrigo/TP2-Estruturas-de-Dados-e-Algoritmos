def contar_livros_impares(fila):
    contador = 0
    
    for livro in fila:
        if livro % 2 != 0:  # Verifica se o número é ímpar
            contador += 1
    
    return contador


# Uso
if __name__ == "__main__":
    fila_livros = [101, 102, 103, 104, 105, 106, 107]
    print("Número de livros com identificação ímpar:", contar_livros_impares(fila_livros))
