for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    x = min(a, b)
    x = 2 * x
    x = max(x, max(a, b))
    print(x * x)
