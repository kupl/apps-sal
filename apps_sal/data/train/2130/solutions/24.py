numeroColores = int(input())
listaNumColores = []
for i in range(0, numeroColores):
    listaNumColores.append(int(input()))
conclusion = 1
anterior = listaNumColores[0]
for (i, numeroColores) in enumerate(listaNumColores[1:]):
    anterior += 1
    conteo1 = 1
    conteo2 = 1
    for j in range(numeroColores - 1):
        conclusion = conclusion * anterior
        anterior += 1
        conteo1 = conteo1 * conteo2
        conteo2 += 1
    conclusion = conclusion // conteo1
if conclusion > 1000000007:
    conclusion = conclusion % 1000000007
print(conclusion)
