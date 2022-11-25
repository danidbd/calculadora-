def soma(num_1, num_2):
    return num_1 + num_2

def subtracao(num_1, num_2):
    return num_1 - num_2

def multiplicacao(num_1, num_2):
    return num_1 * num_2

def divisao(num_1, num_2):
    return num_1 / num_2

print("\n Entre:\n a para adição, \n s para subtraçã, \n m para multipliacação \n d para divição")

a=float(input("Primeiro numero :"))
b=float(input("Segundo numero: "))

escolha=input("Entre com a operação desejada:")


if escolha == 'a':
    print(soma (a, b))

if escolha =='s':
    print(subtracao(a, b))

if escolha == 'm':
    print(multiplicacao(a, b))

if escolha == 'd':
    print(divisao(a, b))    