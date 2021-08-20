for _ in range(int(input())):
    n = int(input())
    t = n
    s = 0
    while t > 0:
        s = s + t * t
        t = t - 2
    print(s)
