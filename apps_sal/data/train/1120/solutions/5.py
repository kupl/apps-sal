for _ in range(int(input())):
    r, c = map(int, input().split())
    x, y = map(int, input().split())
    print(max(x + y, r - x - 1 + y, c - y - 1 + x, r - x - 1 + c - y - 1))
