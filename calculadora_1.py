print("\n Entre:\n  a para adição, \n s para subtraçã, \n m para multipliacação \n d para divição")

a=float(input("Primeiro numero :"))
b=float(input("Segundo numero: "))

escolha=input("Entre com a operação desejada:")


if escolha == 'a':
    print(a+b)

if escolha =='s':
    print(a-b)

if escolha == 'm':
    print(a*b)

if escolha == 'd':
    print(a/b)
