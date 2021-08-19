for _ in range(int(input())):
    (a, b, c) = list(map(int, input().split()))
    i = 0
    d = 0
    while d <= c:
        d = a * i + b
        i = i + 1
    print(d - a)
