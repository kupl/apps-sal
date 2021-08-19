
def getSum(a, b):

    cont = 0
    for i in range(0, len(a)):
        cont += (a[i] + 1) / (b[i] + 1)

    return cont


n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ordenadoB = []
ordenadoA = []
for i in range(0, len(a)):
    ordenadoB.append((i, b[i]))
    ordenadoA.append((i, a[i]))

ordenadoB = sorted(ordenadoB, key=lambda x: x[1])
ordenadoA = sorted(ordenadoA, key=lambda x: x[1], reverse=True)

res = []
# print(ordenadoB, ordenadoA)
for i in range(0, len(ordenadoA)):
    res.append((ordenadoB[i][0], ordenadoA[i][1]))

res = sorted(res, key=lambda x: x[0])
for i in res:
    print(i[1], end=" ")

print('')
