try:
    t = int(input())
    for i in range(t):
        l = list(map(int, input().split()))
        n = l[0]
        p = l[1]
        if n == 1 or n == 2:
            print(p ** 3)
        elif n % 2 == 0:
            print((p - int(n / 2) + 1) ** 2 + (p - n) * (p - int(n / 2) + 1) + (p - n) ** 2)
        else:
            print((p - int(n / 2)) ** 2 + (p - n) * (p - int(n / 2)) + (p - n) ** 2)
except Exception:
    pass
