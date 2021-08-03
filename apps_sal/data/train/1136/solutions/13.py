try:
    for _ in range(int(input())):
        n, k = map(int, input().split())
        if n % 2 == 1:
            print((n // 2 + 1) * k)
        else:
            print((n // 2) * k)
except:
    pass
