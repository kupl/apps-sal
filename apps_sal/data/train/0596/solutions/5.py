t = int(input().strip())
m = 1000000007
for _ in range(t):
    (n, k) = [int(x) for x in input().strip().split()]
    if n == 0:
        ans = k * (k - 1) % m
    elif k % 2 == 0:
        ans = (n * n % m + k * n % m + k * (k - 2) // 4 % m) % m
    else:
        ans = (n * n % m + (k - 1) * n % m + (k + 1) * (k - 1) // 4 % m) % m
    print(ans)
