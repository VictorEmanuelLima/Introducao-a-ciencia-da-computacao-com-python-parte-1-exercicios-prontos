x = int(input("digite a largura: "))
y = int(input("digite a altura: "))
i = 1

while i <= y:
    j = 1
    if i == 1 or i == y:
        while j <= x:
            print("#", end = "")
            j += 1
    else:
        j = 1
        while j <= x:
            if j == 1 or j == x:
                print("#", end = "")
            else:
                print(" ", end = "")  
            j += 1
    print()
    i += 1

    
