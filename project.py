# Miguel Pasadinhas (http://www.github.com/pasadinhas/)

from NASA import *
def temperaturas(c, l):
    
    # Devolve a temperatura no ponto (c,l)
    def temperatura(c, l):
        
        # Devolve uma lista com as coordenadas (c, l) dos pontos que formam um quadrado de 
        # lado = (2*dist + 1) centrado em (c, l). Note-se que esta função devolve um também os pontos
        # "interiores", mas não é necessário remove-los porque eles irão devolver ' ' logo nao afectam os
        # calculos. Se quisessemos remover esses pontos podiamos simplesmente calcular os pontos à distancia
        # (distancia - 1) e remove-los da lista anterior.
        def cria_lista_pontos_distancia(c, l, dist):
                result = []
                # Percorrem-se as colunas:
                for coluna in range(c - dist , c + dist + 1):
                    # Para cada coluna percorrem-se as linhas:
                    for linha in range(l - dist, l + dist + 1):
                        # Verificação se o ponto pertence ao mapa enviado pelo satélite
                        if ponto_pertence_mapa(coluna, linha):
                            result = result + [(coluna, linha)]
                return result
            
        # Recebe uma lista de pontos e devolve uma lista com as temperaturas nesses pontos
        # Note-se que se a comunicação com o satelite devolver ' ', a temperatura desse ponto 
        # nao será adicionada à lista
        def cria_lista_temperaturas(lst):
            res = []
            for ponto in lst:
                if conteudo(ponto[0], ponto[1]) != ' ':
                    res = res + [conteudo(ponto[0], ponto[1])]
            return res
        
        # Se o satélite devolve uma temperatura para o ponto (c, l), entao devolvemos essa temperatura
        if conteudo(c, l) != ' ':
            return conteudo(c, l)
        # Caso o satélite nao devolva uma temperatura calcula-se a temperatura média dos pontos circundantes 
        # (distancia = 1) do ponto (c, l). Nesta fase não se devolve logo a temperatura, guarda-se numa 
        # variavel e devolve-se no fim pois esse valor será necessário para uma operação nesta função
        # (adicionar o valor à lista das temperaturas que foram calculadas)
        else:
            pontos_circundantes = cria_lista_pontos_distancia(c, l, 1)
            temperaturas_pontos = cria_lista_temperaturas(pontos_circundantes)
            # Se pelo menos um dos pontos circundantes tinha temperatura definida 
            # devolve-se a média das temperaturas
            if temperaturas_pontos != []:
                temp = media_elementos_lista(temperaturas_pontos)
            # Caso contrario, devolve a ultima temperatura registada (se esta existir)
            else:
                # Verificação se existe alguma temperatura já registada e atribuição da ultima registada
                # ao ponto em questão
                if lista_temperaturas != []:
                    temp = lista_temperaturas[len(lista_temperaturas) - 1]
                # Se não houver uma temperatura registada calcula-se a média das temperaturas dos pontos a 
                # uma distancia superior à anterior (e repete-se até haver um ponto com temperatura definida)
                else:
                    distancia = 2
                    while temperaturas_pontos == []:
                        pontos_circundantes = cria_lista_pontos_distancia(c, l, distancia)
                        temperaturas_pontos = cria_lista_temperaturas(pontos_circundantes)
                        distancia = distancia + 1
                    temp = media_elementos_lista(temperaturas_pontos) 
        # Adiciona à lista das temperaturas calculadas um tuplo com um tuplo com as coordenadas do ponto e 
        # a temperatura para ele calculada
        temperaturas_calculadas.append(((c,l),temp))
        # Equivalente a: temperaturas_calculadas[len(temperaturas_calculadas):] = [((c,l),temp)]
        return temp

    # Devolve uma lista com 3 tuplos correspondentes às coordenadas dos pontos inicial,
    # de mudança de direcção e final, respectivamente 
    def caminho(c, l):
        res = [(c, l)]
        coluna_media = dimensoes()[0] // 2
        res = res + [(coluna_media, l)]
        linha_media = dimensoes()[1] // 2
        if l > linha_media:
            res = res + [(coluna_media, 0)]
        else:
            res = res + [(coluna_media, dimensoes()[1])]
        return res    
    
    # Devolve a média dos elementos de uma lista de numeros
    def media_elementos_lista(lst):
        def soma_elementos_lista(lst):
            soma = 0
            for e in lst:
                soma = soma + e
            return soma
        return soma_elementos_lista(lst) / len(lst)
    
    # Devolve um valor lógico correspondente a se o ponto (c, l) pertence, ou não, às dimensoes do mapa
    def ponto_pertence_mapa(c, l):
        return 0 <= c <= dimensoes()[0] and 0 <= l <= dimensoes()[1]


    # Verificação se o ponto fornecido pelo utilizador pertence ao mapa
    if not ponto_pertence_mapa(c, l):
        raise ValueError("Ponto fora dos limites do mapa")
    
    # A variavel resultado (que vai ser devolvida no final da funçao adquire aqui a 
    # informação sobre o caminho a seguir
    resultado = caminho(c, l)
    
    # Esta lista vai conter a temperatura de cada ponto do caminho
    lista_temperaturas = []
    
    # Esta lista vai conter tuplos cujo primeiro elemento corresponde a um tuplo com as coordenas dum ponto 
    # para os quais a função conteudo devolveu ' ' e o segundo elemento à temperatura calculada para esse ponto
    temperaturas_calculadas = []
    
    # Movimento Horizontal:
    # Incremento da coluna se a coluna do ponto inicial for inferior à do ponto intermédio
    # Decremento da coluna se a coluna do ponto inicial for superior à do ponto intermédio

    if resultado[0][0] <= resultado[1][0]:
        sentido = 1 # Incremento
    else:
        sentido = -1 # Decremento
    # Note-se que este ciclo que percorre as colunas começa na coluna do ponto inicial, e desloca-se até
    # à coluna do ponto intermédio (à qual é somada a variavel sentido porque o for é exclusivo)
    for i in range(resultado[0][0], resultado[1][0] + sentido, sentido):
        lista_temperaturas = lista_temperaturas + [temperatura(i, l)]
    
    # Movimento Vertical:
    # Incremento da linha se a linha do ponto inicial for inferior à do ponto final
    # Decremento da linha se a linha do ponto inicial for superior à do ponto final   
    
    if resultado[0][1] < resultado[2][1]:
        sentido = 1
    else:
        sentido = -1
    # Note-se que este ciclo que percorre as linhas começa na linha do ponto inicial (somada com a variavel
    # sentido para nao repetir o ponto de viragem) e desloca-se até à linha do ponto final (à qual é 
    # somada a variavel sentido porque o for é exclusivo)    
    for j in range(resultado[0][1] + sentido, resultado[2][1] + sentido, sentido):
        lista_temperaturas = lista_temperaturas + [temperatura(i, j)]
    
    # Devolve-se a variavel resultadado (que contem o caminho) juntamente com a media das temperaturas
    # e a lista das temperaturas calculadas
    return resultado + [media_elementos_lista(lista_temperaturas), temperaturas_calculadas]