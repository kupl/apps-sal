T = int(input())
for i in range(0, T):
    (N, K) = [int(N) for N in input().split()]
    a = input().split()
    b = []
    for j in range(0, K):
        x = input().split()
        for t in range(1, len(x)):
            b.append(x[t])
    r = 0
    for r in range(0, len(a)):
        if b.__contains__(a[r]):
            print('YES', end=' ')
        else:
            print('NO', end=' ')
    print(' ')
