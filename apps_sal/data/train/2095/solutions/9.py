from collections import deque


# ver si hay un camino que llega a el a partir
# de su padre entonces hay un ciclo


def Padre(x, padre):
    while x != padre[x]:
        x = padre[x]
    return x


def DFS(x, color, padre, ciclos, adyacentes, raiz):
    color[x] = 1  # nodo gris
    for y in adyacentes[x]:
        # el adyacente es blanco
        if color[y] == 0:
            DFS(y, color, padre, ciclos, adyacentes, raiz)
            padre[y] = x

        elif color[y] == 2:
            padre[y] = x
        # ese adyacente es gris entonces <u,v>  rista de retroceso
        else:
            if y == x and not raiz:
                raiz = x
            else:
                ciclos.append([x, y])
    color[x] = 2  # nodo negro


def Solucion():
    n = int(input())
    A = list(map(lambda x: int(x)-1, input().split()))

    padre = [x for x in range(0, n)]
    ciclosC = 0
    ciclos = deque([])
    root = []

    # ir haciendo Merge a cada arista
    for i in range(0, n):

        p = Padre(A[i], padre)
        # Si dicha arista perticipa en un ciclo
        if p == i:
            # Si es un ciclo del tipo raiz y no hay raiz
            if not root and (i == A[i]):
                root = [i, A[i]]
            else:
                ciclos.append([i, A[i]])
                ciclosC += 1
        # Si no hay ciclo
        else:
            padre[i] = A[i]

    print(str(ciclosC))
    # si existe al menos un ciclo diferente d raiz
    if ciclosC:
        i = 0
        # si no hay raiz el primer ciclo lo hago raiz
        if not root:
            root = ciclos.popleft()
            i = 1

        # los restantes ciclos hago que su padre sea la raiz
        while ciclos:
            ciclo = ciclos.popleft()
            padre[ciclo[0]] = root[0]

    PC = [x + 1 for x in padre]
    print(*PC, sep=" ")


Solucion()


# Casos de prueba:
# 4
# 2 3 3 4
# respuesta
# 1
#  2 3 3 3

# 5
# 3 2 2 5 3
# respuesta
# 0
# 3 2 2 5 3

# 8
# 2 3 5 4 1 6 6 7
# respuesta
# 2
# 2 3 5 4 1 4 6 7

# 200000
# hacer con el generador

