# Definir as funções para as operações matemáticas

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# Mostrar as opções de operação disponíveis
print("Selecione a operação desejada.")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Obter entrada do usuário para a operação desejada
opcao = input("Digite sua opção (1/2/3/4): ")

# Obter entrada do usuário para os números a serem calculados
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Realizar a operação escolhida
if opcao == '1':
    print(numero1, "+", numero2, "=", add(numero1,numero2))

elif opcao == '2':
    print(numero1, "-", numero2, "=", subtract(numero1,numero2))

elif opcao == '3':
    print(numero1, "*", numero2, "=", multiply(numero1,numero2))

elif opcao == '4':
    print(numero1, "/", numero2, "=", divide(numero1,numero2))
else:
    print("Opção inválida")