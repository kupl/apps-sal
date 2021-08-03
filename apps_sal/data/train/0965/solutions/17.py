t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    if n == 0:
        print(0, 0)
    elif k == 0:
        print(0, n)
    else:
        print(n // k, n % k)
