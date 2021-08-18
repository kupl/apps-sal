for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print(*[2, 1])
    elif n == 3:
        print(*[2, 3, 1])
    else:
        arr = list(range(1, n + 1))
        for i in range(1, n, 2):
            if n % 2 == 1 and n - i == 2:
                arr[i - 1], arr[i], arr[i + 1] = arr[i], arr[i + 1], arr[i - 1]
                break
            else:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        print(*arr)
