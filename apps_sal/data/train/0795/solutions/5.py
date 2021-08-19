# cook your dish here
for _ in range(int(input())):
    N, K, L = map(int, input().split())
    if (K * L < N):
        print(-1)
    elif (K == 1 and N > 1):
        print(-1)
    else:
        s = 1
        for i in range(1, N + 1):
            if s > K:
                s = 1
                print(s, end=' ')
            else:
                print(s, end=' ')
            s = s + 1
    print("")
