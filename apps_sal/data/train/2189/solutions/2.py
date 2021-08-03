import sys
readline = sys.stdin.readline


T = int(readline())
Ans = [None] * T

for qu in range(T):
    N = int(readline())
    A = list(map(int, readline().split()))
    A.sort()
    if N == 1:
        Ans[qu] = 'T'
    elif N == 2:
        if A[0] == A[1]:
            Ans[qu] = 'HL'
        else:
            Ans[qu] = 'T'
    elif A[-1] > sum(A[:-1]):
        Ans[qu] = 'T'
    else:
        if sum(A) % 2 == 0:
            Ans[qu] = 'HL'
        else:
            Ans[qu] = 'T'


print('\n'.join(Ans))
