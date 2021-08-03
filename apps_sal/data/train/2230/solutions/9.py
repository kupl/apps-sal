n = int(input())
p = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m = int(input())
pos = list(map(int, input().split()))

fut = list(zip(p, a, b))
fut = list(fut)


def sravni(elem):
    return elem[0]


fut.sort(key=sravni)

vz = []
for i in range(n):
    vz.append(False)

lastc = [0, 0, 0]
result = ""
for poset in pos:
    ctoim = -1
    for i in range(lastc[poset - 1], n):
        if vz[i] == False:
            if fut[i][1] == poset or fut[i][2] == poset:
                vz[i] = True
                ctoim = fut[i][0]
                lastc[poset - 1] = i + 1
                break
    if ctoim == -1:
        lastc[poset - 1] = n + 1
    result += str(ctoim) + " "
print(result)
