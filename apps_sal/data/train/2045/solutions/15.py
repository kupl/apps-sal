

from sys import stdin

inp = stdin.readline

n, m = list(map(int, inp().split()))
ans = [0] * (n + 1)
alive = [(i + 1) for i in range(n + 2)]

while m:
    m -= 1
    l, r, x = list(map(int, inp().split()))
    i = l
    while i <= r:
        if ans[i] == 0 and i != x:
            ans[i] = x
        temp = alive[i]
        if i < x:
            alive[i] = x
        else:
            alive[i] = r + 1
        i = temp

print(*ans[1:])
