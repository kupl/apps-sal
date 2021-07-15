import sys
readline = sys.stdin.readline

T = int(readline())
MOD =  998244353
Ans = [None]*T
for qu in range(T):
    N, K = map(int, readline().split())
    A = [0] + list(map(int, readline().split())) + [0]
    B = list(map(int, readline().split()))
    C = [None]*(N+1)
    for i in range(1, N+1):
        C[A[i]] = i
    ans = 1
    for b in B[::-1]:
        bi = C[b]
        res = 0
        if A[bi-1]:
            res += 1
        if A[bi+1]:
            res += 1
        A[bi] = 0
        ans = ans*res%MOD
    Ans[qu] = ans
print('\n'.join(map(str, Ans))) 
