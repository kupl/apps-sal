import math
for _ in range(int(input())):
    n = int(input())
    s = int(math.sqrt(n))
    ans = 0
    for i in range(1, s + 1):
        ans += n // i
    ans = ans * 2 - s * s
    g = math.gcd(n * n, ans)
    print(str(ans // g) + '/' + str(n * n // g))
