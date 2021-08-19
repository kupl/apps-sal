try:
    n = int(input())
    l = [int(i) for i in range(1, n + 1)]
    cnt = 0
    for i in range(1, n + 1):
        for j in range(1, n // i + 1):
            if 1 <= n - i * j <= n:
                cnt += 1
    print(cnt)
except EOFError as e:
    pass
