T = int(input())
while T > 0:
    (X, N) = input().split()
    X = int(X)
    N = int(N)
    sum = 0
    for i in range(X, N, 1):
        if i % X == 0:
            sum = sum + i
    T = T - 1
    print(sum)
