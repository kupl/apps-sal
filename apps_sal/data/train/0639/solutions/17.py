# cook your dish here
# cook your dish here
from collections import Counter
T = int(input())
for _ in range(T):
    n = input()
    c = 0
    r = Counter(n)
    L = []
    for j in r.keys():
        L.append(r[j])
    L.sort()
    if len(L) >= 4 and L[1] + L[2] != L[3]:
        temp = L[0]
        L[0] = L[1]
        L[1] = temp
    fl = True
    if len(L) >= 3:
        for i in range(len(L) - 2):
            if L[i + 2] != L[i] + L[i + 1]:
                fl = False
    if fl:
        print('Dynamic')
    else:
        print('Not')
