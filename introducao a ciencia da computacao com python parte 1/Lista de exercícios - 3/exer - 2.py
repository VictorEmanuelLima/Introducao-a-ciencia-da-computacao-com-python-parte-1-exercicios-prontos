n = int(input("Digite o valor de n: "))
i = 1
e = i
while i <= n:
    if e % 2 != 0:
        print(e)
        i = i + 1
        e = e + 1
    else:
        e = e + 1
