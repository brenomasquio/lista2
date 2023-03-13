num = int(input("Digite um número inteiro: "))
while True:
    limite = int(input("Digite o limite da tabuada: "))
    for i in range(1, limite+1):
        print(num, "x", i, "=", num*i)
    continuar = input("Deseja continuar? (s/n) ")
    if continuar.lower() != "s":
        break
