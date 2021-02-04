n = int(input("Digite um número inteiro: "))
a = n % 10

i = len(str(n))
while i != 1:
    i = i - 1
    a = a + (n // (10 ** i))
    n = n % (10 ** i)
              

print(a)
            
   
        
