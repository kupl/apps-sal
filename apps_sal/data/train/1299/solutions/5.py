from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    A = []
    L = list(map(int, input().split()))
    i = 0
    while(i < n):
        if i == n - 1:
            A.append(L[i])
        else:
            if L[i] == L[i + 1]:
                A.append(L[i + 1])
                i = i + 1
            else:
                A.append(L[i])
        i += 1
    count = Counter(A)
    z = []
    maxvalue = max(count.values())
    for k, v in list(count.items()):
        if v == maxvalue:
            z.append(k)
    print(min(z))
