import sys
readline = sys.stdin.readline

T = int(readline())
Ans = ['NO'] * T
for qu in range(T):
    N, K = map(int, readline().split())
    S = [-1 if s == '?' else int(s) for s in readline().strip()]
    L = [-1] * K
    for i in range(N):
        j = i % K
        si = S[i]
        if L[j] == -1:
            L[j] = si
        elif S[i] == -1:
            continue
        else:
            if L[j] != si:
                break
    else:
        one = 0
        zero = 0
        minus = 0
        for l in L:
            if l == 1:
                one += 1
            elif l == 0:
                zero += 1
            else:
                minus += 1

        if one < zero:
            one, zero = zero, one

        if zero + minus >= one:
            Ans[qu] = 'YES'


print('\n'.join(Ans))
