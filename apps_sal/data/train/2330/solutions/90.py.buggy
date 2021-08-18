def printn(x): return print(x, end='')
def inn(): return int(input())


def inl(): return list(map(int, input().split()))
def inm(): return map(int, input().split())
def ins(): return input().strip()


DBG = True  # and False
BIG = 10**18
R = 10**9 + 7


def ddprint(x):
    if DBG:
        print(x)


s = ins()
n = len(s)
s = '0' + s
if s[1] == '0' or s[n] == '1':
    print(-1)
    return
for i in range(1, n):
    if s[i] != s[n - i]:
        print(-1)
        return
e = []
p = 1
for i in range(2, n + 1):
    if s[i] == '1' or i == n:
        for j in range(p, i):
            e.append((j, i))
        p = i
for z in e:
    print("{} {}".format(z[0], z[1]))
