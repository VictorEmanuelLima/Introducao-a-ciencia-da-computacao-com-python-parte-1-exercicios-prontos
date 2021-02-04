num = int(input('Digite um número inteiro: '))
num = num % 1000000
num = num % 100000
num = num % 10000
num = num % 1000
num = num % 100
num = num // 10
print('O dígito das dezenas é',num)
