t = int(input())
while t > 0:
    s = int(0)
    n = int(input())
    while n > 0:
        (a, b) = list(map(int, input().split()))
        if b - a > 5:
            s = s + 1
        n = n - 1
    t = t - 1
    print(s)
