num = int(input("Digite um número inteiro positivo: "))
print("Fatores primos de", num, ":")
divisor = 2
while num > 1:
    if num % divisor == 0:
        num /= divisor
        print(divisor)
    else:
        divisor += 1
