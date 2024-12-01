def contar_pedidos_pares(pilha_de_pedidos):
    contador_pares = 0

    # Percorre a pilha para verificar cada número
    for pedido in pilha_de_pedidos:
        if pedido % 2 == 0:  # Verifica se o número é par
            contador_pares += 1

    return contador_pares


# Uso
if __name__ == "__main__":
    # Exemplo
    pilha_pedidos = [101, 202, 303, 404, 505, 606]

    print("Pilha de pedidos:", pilha_pedidos)
    qtd_pares = contar_pedidos_pares(pilha_pedidos)
    print("Quantidade de pedidos pares:", qtd_pares)
