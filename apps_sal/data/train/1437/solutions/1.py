from math import ceil, sqrt, floor
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    x = a[0] * a[n - 1]
    div = []
    for i in range(2, floor(sqrt(x)) + 1):
        if x % i == 0:
            div.append(i)
            y = x // i
            if i != y:
                div.append(y)
    div.sort()
    if a == div:
        print(x)
    else:
        print(-1)
