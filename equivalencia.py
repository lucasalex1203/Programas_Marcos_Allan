def sao_relacoes_equivalentes(relacao1, relacao2):
    return set(relacao1) == set(relacao2)

# Exemplo de uso
relacao1 = {(1, 2), (2, 3), (3, 4)}
relacao2 = {(3, 4), (2, 3), (1, 2)}

if sao_relacoes_equivalentes(relacao1, relacao2):
    print("As relações são equivalentes.")
else:
    print("As relações não são equivalentes.")
