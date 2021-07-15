import sys

sys.setrecursionlimit(10 ** 5)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def solve():
    pre = []
    pos = []
    for a in aa:
        if a > m: pos.append(a)
        else: pre.append(a)
    pos.sort(reverse=True)
    pre.sort(reverse=True)

    cs = [0]
    for a in pre: cs.append(cs[-1] + a)
    pre = cs
    cs = [0]
    for a in pos: cs.append(cs[-1] + a)
    pos = cs

    ans = 0
    for i in range(len(pre)):
        j = min((n - i - 1) // (d + 1) + 1, len(pos) - 1)
        cur = pre[i] + pos[j]
        ans = max(ans, cur)

    print(ans)

n,d,m=MI()
aa=MI()
solve()

