def fecho_reflexivo(conjunto):
    fecho = set(conjunto)  # Começamos com o conjunto original

    for elemento in conjunto:
        fecho.add((elemento, elemento))

    return fecho

# Exemplo de uso
conjunto_original = {1, 2, 3}
resultado = fecho_reflexivo(conjunto_original)

print("Conjunto original:", conjunto_original)
print("Fecho reflexivo:", resultado)
