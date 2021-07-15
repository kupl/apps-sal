for _ in range(int(input())):
    x, n = map(int, input().split())
    r = 0
    i = 1
    while x*i < n:
        r += x*i
        i += 1
    print(r)
