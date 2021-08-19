t = int(input())
for _ in range(t):
    (n, k) = map(int, input().split())
    if n == 1:
        print(1)
    else:
        r = (2 + k) * (n // 2)
        if n % 2 != 0:
            r += 1 + 2 * k
        print(r)
