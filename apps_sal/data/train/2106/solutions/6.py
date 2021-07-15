from functools import reduce

n = int(input())
cards = [list(map(int, input().split()[1:])) for i in range(n)]
mid = [c[len(c) >> 1] for c in cards if len(c) & 1 == 1]
a, b = 0, 0
add = lambda x=0, y=0: x + y
for c in cards:
    m = len(c) >> 1
    a += reduce(add, c[:m] or [0])
    b += reduce(add, c[m + (len(c) & 1):] or [0])
mid.sort(reverse=True)
a += reduce(add, mid[::2] or [0])
b += reduce(add, mid[1::2] or [0])
print(a, b)

