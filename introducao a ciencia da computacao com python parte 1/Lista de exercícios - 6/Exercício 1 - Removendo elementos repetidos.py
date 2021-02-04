def remove_repetidos(lista):
    lista = sorted(lista)
    x = len(lista)
    d = 0
    for i in lista:
        c = 0
        
        while c < len(lista) and d < len(lista):
            if i == lista[c] and d != c:
                del (lista[c])
            c += 1
            if len(lista) < x:
                c -= 1
                
            x = len(lista)
        d += 1
    return lista
