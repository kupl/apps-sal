n, k = list(map(int, input().split()))
L = list(map(int, input().split()))
p = sum(L)
if p % k == 0:
    M = []
    summa = 0
    count = 0
    f = True
    for i in L:
        if summa + i == p // k:
            M.append(count + 1)
            summa = 0
            count = 0
        elif summa + i > p // k:
            f = False
        else:
            summa += i
            count += 1
    if f and len(M) == k:
        print('Yes')
        print(*M)
    else:
        print('No')
else:
    print('No')
