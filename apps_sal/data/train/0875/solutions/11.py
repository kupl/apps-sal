from itertools import chain


def R(): return list(map(int, input().split()))


t = int(input())
for _ in range(t):
    n, *z = R()
    u = set(chain.from_iterable((x, -x) for x in R()))
    v = set(x + y for x in z for y in u)
    if 0 in v:
        print(1)
    elif u <= v:
        print(2)
    else:
        print(0)
