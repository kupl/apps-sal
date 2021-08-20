try:
    for _ in range(int(input())):
        (n, k) = [*map(int, input().split())]
        t = [*map(int, input().split())]
        a = max(t) + k
        b = min(t) - k
        if b > 0:
            print(abs(a - b))
        else:
            print(abs(b - a))
except:
    pass
