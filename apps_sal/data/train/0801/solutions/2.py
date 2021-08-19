# cook your dish here
from collections import Counter
for _ in range(int(input())):

    n = int(input())
    x = sorted(map(int, input().split()))
    y = sorted(map(int, input().split()))
    a = Counter(x)
    b = Counter(y)
    c = a + b
    l = []
    mini = min(x[0], y[0])
    for i in c.keys():

        if c[i] % 2 == 1:
            print(-1)
            break
        else:
            l.extend([i] * (abs(a[i] - b[i]) // 2))

    else:
        l.sort()
        cost = 0
        for i in range((len(l) // 2)):

            cost = cost + min(l[i], 2 * mini)

        print(cost)
