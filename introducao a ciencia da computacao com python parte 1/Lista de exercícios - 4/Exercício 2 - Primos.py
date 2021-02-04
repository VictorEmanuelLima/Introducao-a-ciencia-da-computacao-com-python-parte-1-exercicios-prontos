def éprimo (n):
    cont = 0
    i = 0

    while i <= n or cont < 2:
        i = i + 1
        x = n % i
        if x == 0:
            cont = cont + 1

    if cont <= 2:
        return n
    
            
def maior_primo(x):
    while x >= 2:
        if éprimo(x) == x:
            return x
        else:
            x = x -1
        
