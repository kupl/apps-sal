for _ in range(int(input())):
    (N, K, L) = map(int, input().split(' '))
    if N == 1 and K == 1:
        print(1)
    elif K * L >= N and K != 1:
        for i in range(N):
            print(i % K + 1, end=' ')
        print()
    else:
        print(-1)
