def verifica_pertinencia():
    conjunto_usuario = input("Digite um conjunto (ex: 1, 2, 3): ")
    try:
        conjunto = set(map(int, conjunto_usuario.split(',')))
    except ValueError:
        print("Erro: Certifique-se de que você digitou números separados por vírgulas.")
        return
    elemento = int(input("Digite um elemento para verificar pertinência: "))
    if elemento in conjunto:
        print(f"{elemento} pertence ao conjunto {conjunto}")
    else:
        print(f"{elemento} não pertence ao conjunto {conjunto}")
if __name__ == "__main__":
    verifica_pertinencia()
