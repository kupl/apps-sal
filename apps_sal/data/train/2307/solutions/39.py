import sys


def IN_I(): return int(sys.stdin.readline().rstrip())
def IN_LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def IN_S(): return sys.stdin.readline().rstrip()
def IN_LS(): return list(sys.stdin.readline().rstrip().split())


INF = float('inf')
MOD = 10**9 + 7


N, A, B = IN_LI()
X = IN_LI()

ans = 0
for i in range(N - 1):
    d = X[i + 1] - X[i]
    if A * d >= B:
        ans += B
    else:
        ans += A * d
print(ans)
