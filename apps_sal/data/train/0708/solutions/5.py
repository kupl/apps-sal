m = int(1e9 + 7)
for _ in range(int(input())):
    n, a = list(map(int, input().split()))
    j = 1
    ans = 0
    for i in range(1, n + 1):
        k = pow(a, 2 * i - 1, m)
        ans += k
        a = (a * k) % m
    print(ans % m)
