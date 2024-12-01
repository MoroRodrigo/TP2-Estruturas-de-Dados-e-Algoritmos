def contar_pedidos_impares(pilha_de_pedidos):
    contador_impares = 0

    # Percorre a pilha para verificar cada número
    for pedido in pilha_de_pedidos:
        if pedido % 2 != 0:  # Verifica se o número é ímpar
            contador_impares += 1

    return contador_impares


# Uso
if __name__ == "__main__":
    # Exemplo
    pilha_pedidos = [101, 202, 303, 404, 505, 606]

    print("Pilha de pedidos:", pilha_pedidos)
    qtd_impares = contar_pedidos_impares(pilha_pedidos)
    print("Quantidade de pedidos ímpares:", qtd_impares)
