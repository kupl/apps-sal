from collections import defaultdict


def def_value():
    return 0


(n, m) = map(int, input().split())
for i in range(m):
    x = int(input())
    if x <= n + 1 or x > 3 * n:
        print(0)
    elif x <= 2 * n + 1:
        print(x % (n + 1))
    else:
        print(3 * n + 1 - x)
