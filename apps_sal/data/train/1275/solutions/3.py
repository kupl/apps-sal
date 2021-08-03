T = int(input())
ans = []

for _ in range(T):
    N, M = [int(i) for i in input().split()]
    P = [int(i) for i in input().split()]

    left_most = N - 1
    right_most = 0
    for i in range(M):
        if(P[i] > right_most):
            right_most = P[i]
        if(P[i] < left_most):
            left_most = P[i]
    s = ''
    for i in range(N):
        s += str(max(abs(i - left_most), abs(i - right_most))) + ' '
    ans.append(s)

for i in ans:
    print(i)
