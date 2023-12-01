# Série alternante de potências de 3

soma = 0
i = 0
vetor = []

while i < 10:
    valor = (-1) ** i * 3 ** (i + 1)
    vetor.append(valor)
    soma += valor
    i += 1

print("Termos da série:", vetor)
print("Soma dos termos:", soma)