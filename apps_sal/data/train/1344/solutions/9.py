# https://www.codechef.com/problems/SMPAIR

T = int(input())

for t in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]
    m = A[0] + A[1]
    for i in range(N):
        for j in range(i + 1, N):
            cur = A[i] + A[j]
            if cur < m:
                m = cur
    print(m)
