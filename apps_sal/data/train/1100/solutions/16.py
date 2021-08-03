for _ in range(int(input())):
    arr = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    c, f = 0, 0
    for i in range(3):
        if (arr[i] > arr2[i]):
            f = 1
            break
        else:
            c = c + arr2[i] - arr[i]
    if (f == 1):
        print(-1)
    else:
        print(c)
