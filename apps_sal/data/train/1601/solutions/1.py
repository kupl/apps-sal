t = int(input())
for _ in range(t):
    (n, p) = map(int, input().strip().split())
    if n <= 2:
        print(p * p * p)
    else:
        m = (n - 1) // 2
        res = (p - m) ** 2 + (p - n) ** 2 + (p - m) * (p - n)
        print(res)
