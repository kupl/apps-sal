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


s = ins()
t = ins()
sacc = [0]
for c in s:
    sacc.append(((1 if c == 'A' else 2) + sacc[-1]) % 3)
tacc = [0]
for c in t:
    tacc.append(((1 if c == 'A' else 2) + tacc[-1]) % 3)
q = inn()
for i in range(q):
    a, b, c, d = inm()
    print('YES' if (sacc[b] - sacc[a - 1]) % 3 == (tacc[d] - tacc[c - 1]) % 3 else 'NO')
