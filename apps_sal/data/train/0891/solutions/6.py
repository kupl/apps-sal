ans = []
(N, M) = [int(i) for i in input().split()]
for i in range(M):
    q = int(input())
    if q <= N:
        s = 0
    elif q <= 2 * N:
        s = q - N - 1
    else:
        s = N - (q - 2 * N - 1)
    ans.append(s)
for i in ans:
    print(i)
