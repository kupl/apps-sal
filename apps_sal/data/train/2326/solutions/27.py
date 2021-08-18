def printn(x): return print(x, end='')
def inn(): return int(input())


def inl(): return list(map(int, input().split()))
def inm(): return map(int, input().split())
def ins(): return input().strip()


DBG = True
BIG = 10**18
R = 10**9 + 7


def ddprint(x):
    if DBG:
        print(x)


n = inn()
a = inl()
b = [(a[i], i) for i in range(n)]
b.sort(reverse=True)
b.append((0, 0))
ans = [0] * n
v = b[0][1]
for i in range(n):
    ans[v] += (i + 1) * (b[i][0] - b[i + 1][0])
    v = min(v, b[i + 1][1])
for i in range(n):
    print(ans[i])
