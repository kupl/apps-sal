for _ in range(int(input())):
    (r, c) = map(int, input().split())
    (x, y) = map(int, input().split())
    r = r - 1
    c = c - 1
    ans = max(max(abs(r - x) + y, abs(c - y) + x), max(x + y, abs(r - x) + abs(c - y)))
    print(ans)
