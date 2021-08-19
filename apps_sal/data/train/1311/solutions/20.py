for _ in range(int(input())):
    a, b = map(int, input().split())
    arr = [0] * a
    for i in range(a):
        arr[i] = i + 1
    x = 0
    b = a - b
    if(b > a // 2):
        x = b - a // 2
        b = a // 2
    # print(b,x)
    for i in range(b):
        arr[(2 * i) + 1] *= -1
    if(a % 2 == 0):
        for i in range(x):
            arr[a - 2 * i - 2] *= -1
    if(a % 2 != 0):
        for i in range(x):
            arr[a - 2 * i - 1] *= -1
    print(*arr)
