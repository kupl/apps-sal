t = int(input())

for i in range(t):
    N, M = map(int, input().split())
    lis = []
    for i in range(N):
        lis.append(10)

    for i in range(M):
        a, b, c = map(int, input().split())
        for i in range(a - 1, b):
            lis[i] = lis[i] * c
    print(sum(lis) // N)
