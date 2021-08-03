for _ in range(int(input())):
    N, K = map(int, input().split())
    ll = list(map(int, input().split()))
    c1 = 0
    c2 = 0
    for i in range(N):
        for j in range(i + 1, N):
            if ll[i] > ll[j]:
                c1 += 1
    for i in range(N):
        for j in range(N):
            if ll[i] > ll[j]:
                c2 += 1
    print(c1 * K + c2 * K * (K - 1) // 2)
