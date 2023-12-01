def fecho_transitivo(pares):
    fecho = set(pares)  # Começamos com o conjunto original

    while True:
        novo_fecho = set(fecho)  # Criamos uma cópia do fecho atual

        for par1 in fecho:
            for par2 in fecho:
                if par1[1] == par2[0]:
                    novo_fecho.add((par1[0], par2[1]))

        if novo_fecho == fecho:
            break  # Se não houver mais adições, o fecho transitivo está completo
        else:
            fecho = novo_fecho

    return fecho

# Exemplo de uso
pares_ordenados = {(1, 2), (2, 3), (3, 4)}
resultado = fecho_transitivo(pares_ordenados)

print("Conjunto original:", pares_ordenados)
print("Fecho transitivo:", resultado)
