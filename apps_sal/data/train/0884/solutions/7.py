import math
t = int(input())
i = 1
while i <= t:
    (x, k) = list(map(int, input().split()))
    lst1 = []
    lst2 = []
    for j in range(2, x + 1):
        if x % j == 0:
            lst1 += [j]
    for l in range(2, k + 1):
        if k % l == 0:
            lst2 += [l]
    a2 = sum(lst2) * x
    a1 = 0
    for p in range(0, len(lst1)):
        a1 = a1 + math.pow(lst1[p], k)
    print(int(a1), a2)
    i += 1
