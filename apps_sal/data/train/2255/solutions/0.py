from collections import Counter as C
def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(mi())


n = ii()
a = li()
oe = [C(), C()]
oe[1][0] = 1
x = 0
ans = 0
for i in range(n):
    x ^= a[i]
    ans += oe[i % 2][x]
    oe[i % 2][x] += 1
print(ans)
