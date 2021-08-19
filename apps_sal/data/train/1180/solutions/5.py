n = int(input())
i = 1
while i <= n:
    (N, K, x, y) = input().split()
    N = int(N)
    K = int(K)
    x = int(x)
    y = int(y)
    if x > y:
        if K % 4 == 1:
            print(N, N - x + y)
        elif K % 4 == 2:
            print(N - x + y, N)
        elif K % 4 == 3:
            print(0, x - y)
        else:
            print(x - y, 0)
    elif x == y:
        print(N, N)
    elif K % 4 == 2:
        print(N, N - y + x)
    elif K % 4 == 1:
        print(N - y + x, N)
    elif K % 4 == 0:
        print(0, y - x)
    else:
        print(y - x, 0)
    i = i + 1
