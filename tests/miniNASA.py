def dimensoes():
    return (10, 6)

colunas = dimensoes()[0]
linhas = dimensoes()[1]

def conteudo(c, l):
    if c > colunas or l > linhas:
        raise IndexError ('MAPA coluna ', c, 'linha ', l, '--> Posicao fora da matriz')
    elif ((c == colunas // 2 - 1 or c == colunas // 2 + 1) and l == linhas):
        return float(l)
    elif l > 2 or (c == 4 and l == 1):
        return ' '
    elif (c <= 2 and l <= 2) :
        return ' '
    else :
        return float(l)

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

