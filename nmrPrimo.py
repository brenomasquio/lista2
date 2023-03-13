numero = int(input("Digite um número inteiro: "))

print("Números primos menores ou iguais a", numero, ":")

for i in range(2, numero+1):
    eh_primo = True
    for j in range(2, i):
        if i % j == 0:
            eh_primo = False
            break
    if eh_primo:
        print(i)
