for _ in range(int(input())):
    x, y = list(map(int, input().split()))

    while(y):
        x, y = y, x % y

    print(2 * x)
