from collections import deque


def Padre(x, padre):
    while x != padre[x]:
        x = padre[x]
    return x


def DFS(x, color, padre, ciclos, adyacentes, raiz):
    color[x] = 1
    for y in adyacentes[x]:
        if color[y] == 0:
            DFS(y, color, padre, ciclos, adyacentes, raiz)
            padre[y] = x
        elif color[y] == 2:
            padre[y] = x
        elif y == x and (not raiz):
            raiz = x
        else:
            ciclos.append([x, y])
    color[x] = 2


def Solucion():
    n = int(input())
    A = list(map(lambda x: int(x) - 1, input().split()))
    padre = [x for x in range(0, n)]
    ciclosC = 0
    ciclos = deque([])
    root = []
    for i in range(0, n):
        p = Padre(A[i], padre)
        if p == i:
            if not root and i == A[i]:
                root = [i, A[i]]
            else:
                ciclos.append([i, A[i]])
                ciclosC += 1
        else:
            padre[i] = A[i]
    print(str(ciclosC))
    if ciclosC:
        i = 0
        if not root:
            root = ciclos.popleft()
            i = 1
        while ciclos:
            ciclo = ciclos.popleft()
            padre[ciclo[0]] = root[0]
    PC = [x + 1 for x in padre]
    print(*PC, sep=' ')


Solucion()
