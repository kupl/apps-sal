for _ in range(int(input())):
    x, y = list(map(int, input().split()))
    a, b = x, y
    while(y):
        x, y = y, x % y
    k = x

    if (a + b) // k != 0:
        print((a + b) // k - 2)
    else:
        print(0)
