n = int(input())
lista = []
for i in range(n):
    lista.append([int(x) for x in input().split()])
lista.sort()

diccionario = dict()
nada = True
last = 0
maximo = 0
for x, i in lista:
    if nada == True:
        for c in range(0, x):
            diccionario[c] = 0
        diccionario[x] = 1
        maximo = 1
        nada = False
        last = x
    else:
        for w in range(last, x):
            diccionario[w] = diccionario[last]
        if i >= x:
            diccionario[x] = 1
        else:
            aux = diccionario[x - i - 1] + 1
            if aux > maximo:
                maximo = aux
            diccionario[x] = aux
        last = x
print(n - maximo)

