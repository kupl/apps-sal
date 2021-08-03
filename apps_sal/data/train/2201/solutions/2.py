def weakness(a, x):
    a = [elem - x for elem in a]
    acumulado = maximo = 0
    for elem in a:
        if acumulado + elem > 0:
            acumulado += elem
        else:
            acumulado = 0
        if acumulado > maximo:
            maximo = acumulado
    acumulado = minimo = 0
    for elem in a:
        if acumulado + elem < 0:
            acumulado += elem
        else:
            acumulado = 0
        if acumulado < minimo:
            minimo = acumulado
    return max(maximo, -minimo)


n, a = input(), list(map(int, input().split()))

inf, sup = min(a), max(a)
for _ in range(70):
    c1, c2 = (2 * inf + sup) / 3, (inf + 2 * sup) / 3
    if weakness(a, c1) < weakness(a, c2):
        sup = c2
    else:
        inf = c1

print(weakness(a, (inf + sup) / 2))
