import sys
readline = sys.stdin.readline

T = int(readline())
Ans = ['NO'] * T

for qu in range(T):
    N = int(readline())
    A = list(map(int, readline().split()))
    S = set()
    for i in range(N):
        S.add((i + A[i]) % N)
    if len(S) == N:
        Ans[qu] = 'YES'
print('\n'.join(map(str, Ans)))
