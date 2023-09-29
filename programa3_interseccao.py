pergunta = "Qual é a intersecção de A = {1, 2, 3} e B = {2, 5, 8}?"
resposta_correta = 2
while True:
    resposta_usuario = int(input(pergunta + " "))
    if resposta_usuario == resposta_correta:
        print("Parabéns! A condição é verdadeira.")
        break
    else:
        print("Ops! A condição é falsa. Tente novamente.")
