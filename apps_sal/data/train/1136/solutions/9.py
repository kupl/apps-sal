for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    if n % 2:
        s = k * (n // 2 + 1)
    else:
        s = k * (n // 2)
    print(s)
