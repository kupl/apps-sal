from functools import reduce
n = int(input())
cards = [list(map(int, input().split()[1:])) for i in range(n)]
mid = sorted((c[len(c) >> 1] for c in cards if len(c) & 1 == 1), reverse=True)


def add(x=0, y=0):
    return x + y


(a, b) = (reduce(add, mid[::2] or [0]), reduce(add, mid[1::2] or [0]))
for c in cards:
    m = len(c) >> 1
    a += reduce(add, c[:m] or [0])
    b += reduce(add, c[m + (len(c) & 1):] or [0])
print(a, b)
