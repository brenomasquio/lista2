num = int(input("Digite um número inteiro positivo: "))
print("Números perfeitos até", num, ":")
for i in range(1, num+1):
    soma_divisores = 0
    for j in range(1, i):
        if i % j == 0:
            soma_divisores += j
    if soma_divisores == i:
        print(i)
