from sys import setrecursionlimit as SRL, stdin
SRL(10 ** 7)
rd = stdin.readline


def rrd():
    return map(int, rd().strip().split())


n = int(rd())
bit = [0] * 200005


def add(x, val):
    while x <= n:
        bit[x] += val
        x += x & -x


def query(x):
    num = 0
    for i in range(30, -1, -1):
        if num + (1 << i) <= n and bit[num + (1 << i)] <= x:
            x -= bit[num + (1 << i)]
            num += 1 << i
    return num + 1


for i in range(1, n + 1):
    add(i, i)
s = list(rrd())
ans = []
for i in range(len(s) - 1, -1, -1):
    q = query(s[i])
    ans.append(q)
    add(q, -q)
ans = ans[::-1]
print(*ans)
