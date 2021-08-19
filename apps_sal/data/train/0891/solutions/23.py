(n, m) = map(int, input().split())
for i in range(m):
    q = int(input())
    if q > n + 1:
        print(q - n - 1) if q < 2 * (n + 1) else print(3 * n - q + 1)
    else:
        print('0')
