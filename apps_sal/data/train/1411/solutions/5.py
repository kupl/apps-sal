for _ in range(int(input())):

    x, r, a, b = map(int, input().split())

    print(x - 1 - x * min(a, b) // max(a, b))
