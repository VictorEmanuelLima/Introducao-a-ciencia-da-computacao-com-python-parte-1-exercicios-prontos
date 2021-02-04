x = int(input("digite a largura: "))
y = int(input("digite a altura: "))
i = 1
while i <= y:
    j = 1
    while j <= x:
        print("#", end = "")
        j += 1
    print()
    i += 1
