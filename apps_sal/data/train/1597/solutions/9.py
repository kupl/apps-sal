import math

for _ in range(int(input())):
    a, m = list(map(int, input().split()))
    f = {1}
    for i in range(2, int(math.sqrt(m)) + 1):
        if m % i == 0:
            f.add(i)
            f.add(m // i)

    total = 0
    l = []
    for i in f:
        p = m - i
        if p % a == 0:
            q = p // a
            if q % i == 0:
                l.append(q)
                total += 1

    print(total)
    if total > 0:
        l.sort()
        print(*l, end=' ')
        print('')

    else:
        print(' ')
