pergunta = "Qual é o resultado de 5 + 3?"
resposta_correta = 8
while True:
    resposta_usuario = int(input(pergunta + " "))
    if resposta_usuario == resposta_correta:
        print("Parabéns! A condição é verdadeira.")
        break
    else:
        print("Ops! A condição é falsa. Tente novamente.")
