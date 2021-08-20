for _ in range(int(input())):
    (n, k) = map(int, input().split())
    sm = k * (k + 1) // 2
    if n < sm:
        print(-1)
        continue
    m = 1
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if n // i >= sm:
                m = max(m, i)
            x = n // i
            if n // x >= sm:
                m = max(m, x)
    print(m)
