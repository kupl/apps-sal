N = int(input())
L, L1, L2 = [], {}, {}
for i in range(0, N):
    x, y = map(int, input().split())
    L.append(x)
    L.append(y)
    if x in L1:
        L1[x] += 1
    elif x not in L1:
        L1[x] = 1
    if y in L2:
        L2[y] += 1
    elif y not in L2:
        L2[y] = 1

L.sort()
persons = 0
s = 0
M = 1000000007
for elem in range(L[0], L[-1] + 1):
    if elem in L1:
        persons += L1[elem]
        deboard = False
    if elem in L2:
        deboard = True

    s += persons
    if deboard:
        persons -= L2[elem]
        deboard = False

print(s % M)
