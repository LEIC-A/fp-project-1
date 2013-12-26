def dimensoes():
    return (80, 30)

colunas = dimensoes()[0]
linhas = dimensoes()[1]

base = 20.0

def conteudo(c, l):
    if c > colunas or l > linhas:
        raise IndexError ('MAPA: coluna ', c, 'linha ', l, '--> Posicao fora da matriz')
    elif l in primos or c in primos:
        return ' '
    elif l < r1(c) :
        return base
    elif l < r2(c) :
        return base - 10
    elif l < r3(c):
        return base - 20
    elif l < r4(c):
        return base - 30
    elif l < r5(c):
        return base - 40
    elif l < r6(c):
        return base - 50
    elif l < r7(c):
        return base - 60
    elif l < r8(c):
        return base - 70
    elif l < r9(c):
        return base - 80
    elif l < r10(c):
        return base - 90
    else:
        return base - 100


def r1 (x):
    return linhas - x * linhas / (colunas * 0.1)

def r2 (x):
    return linhas - x * linhas / (colunas * 0.13)

def r3 (x):
    return linhas - x * linhas / (colunas * 0.2)

def r4 (x):
    return linhas - x * linhas / (colunas * 0.7)

def r5 (x):
    return linhas - x * linhas / (colunas * 0.9)

def r6 (x):
    return ((0.3 - 1) * linhas) / ((1 - 0.12) * colunas) * (x - 0.12 * colunas) + linhas

def r7 (x):
    return ((0.5 - 1) * linhas) / ((1 - 0.12) * colunas) * (x - 0.12 * colunas) + linhas

def r8 (x):
    return ((0.7 - 1) * linhas) / ((1 - 0.12) * colunas) * (x - 0.12 * colunas) + linhas

def r9 (x):
    return ((0.8 - 1) * linhas) / ((1 - 0.12) * colunas) * (x - 0.12 * colunas) + linhas

def r10 (x):
    return ((0.9 - 1) * linhas) / ((1 - 0.12) * colunas) * (x - 0.12 * colunas) + linhas


def crivo (n) :

    def remove_multiplos(lst, n) :

        def pos (lst, n) :
            for i in range (n) :
                if lst[i] > n :
                    return i

        for i in range(len(lst) - 1, pos(lst, n), -1) :
            if lst[i] % n == 0 :
                del(lst[i])

    from math import sqrt

    lista = []
    for i in range(2, n + 1) :
        lista = lista + [i]

    i = 0
    while lista[i] <= sqrt(n) :
        remove_multiplos(lista, lista[i])
        i = i + 1
    return lista




primos = crivo(colunas)

def print_mapa():
    st = "         "
    for y in range(colunas + 1):
        st += str(y) + ','
    print(st)
    for y in range(linhas + 1):
        st = "linha" + str(y) + "-->"
        for x in range(colunas + 1):
            st += str(conteudo(x, y)) + ","
        print(st, "\n")

