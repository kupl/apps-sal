import math
t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    for i in range(0, n):
        l1 = input()
        l.append(l1)
    ind = []
    count = n + 1
    for i in range(0, n):
        x = list(l[i])
        y = x.index('1')
        ind.append(y)
    flag = 0
    for i in range(1, n):
        if ind[i] == ind[i - 1] + 1:
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        print(int(n * (n + 1) / 2))
        continue
    for i in range(2, n):
        for j in range(0, n):
            nl = []
            if j + i > n:
                break
            s = sum(ind[j:j + i])
            f = min(ind[j:j + i])
            if s - i * f == int((i - 1) * i / 2):
                count += 1
    print(count)
