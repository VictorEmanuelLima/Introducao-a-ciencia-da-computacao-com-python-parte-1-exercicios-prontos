import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    somatorio = 0
    for i in range(len(as_a)):
        somatorio += abs(as_a[i] - as_b[i])

    return somatorio / 6
def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    sen = separa_sentencas(texto)
    nusen = 0
    caras = 0
    fras = []
  
    
    n_f= 0
    for a in range(len(sen)):       
        f_aux = separa_frases(sen[a])
        fras.append(f_aux)
        nusen += 1
        caras += len(sen[a])

    tp2 = [] 
    caraf =0
    n_f= 0
    for a in range(len(fras)):
        for b in range(len(fras[a])):
            pala_a = separa_palavras(fras[a][b])
            tp2.append(pala_a)
            caraf += len(fras[a][b])
            n_f += 1
 

    carap = 0
    tp3 = []
    for a in range(len(tp2)):
        for b in range(len(tp2[a])):
            tp3.append(tp2[a][b])
    tp2 = tp3[:]
    np = len(tp2)
    for a in range(len(tp2)):
        for b in range(len(tp2[a])):
            carap += len(str(tp2[a][b]))
    mp = carap / np
    tt = n_palavras_diferentes(tp2) / np
    hl = n_palavras_unicas(tp2) / np
    ms = caras / nusen
    cm = n_f / nusen
    mf = caraf / n_f
    return [mp, tt, hl, ms, cm, mf]
    #pass

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    aux = (ass_cp[:])
    aux.sort()
    for i in range(len(ass_cp)):
        if aux[0] == ass_cp[i]:
            copiah = i
    return copiah

def main():
    assinaturaMain = le_assinatura()
    textos = le_textos()
    
    return  print("O autor do texto " , avalia_textos(textos, assinaturaMain), " está infectado com COH-PIAH")
main()
