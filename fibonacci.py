num = int(input("Digite um número inteiro positivo: "))
fibonacci = [0, 1] # lista que armazenará a sequência de Fibonacci
for i in range(2, num):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print("Sequência de Fibonacci até o", num, "º termo:")
print(fibonacci[:num])
