T = int(input())
for i in range(T):
    N = int(input())
    L = list(map(int, input().split()))[:N]
    L.sort()
    c = 0
    for j in range(N // 2):
        c += abs(L[j] - L[N - j - 1])
    print(c)
