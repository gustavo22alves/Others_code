meucartao = int(input("Digite o número do seu cartão de crédito: "))

cartaolido = 1
encontreimeucartao = False

while cartaolido != 0 and not encontreimeucartao:
    cartaolido = int(input("Digite o próximo número do seu cartão de crédito: "))
    if cartaolido == meucartao:
        encontreimeucartao = True

if encontreimeucartao:
    print("EBA... encontrei essa porra..")
else:
    print("IXI... acho que clonaram meu cartao...")

