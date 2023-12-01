def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

while True:
    try:
        numero = int(input("Digite um número natural para calcular o fatorial: "))
        if numero < 0:
            print("Por favor, digite um número natural ou zero.")
        else:
            break
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

resultado = fatorial(numero)

print(f'O fatorial de {numero} é {resultado}')
