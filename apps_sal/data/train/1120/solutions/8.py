for u in range(int(input())):
    x, y = list(map(int, input().split()))
    a, b = list(map(int, input().split()))
    m = max(y - 1 - b, b)
    r = max(x - a - 1, a)
    print(m + r)
