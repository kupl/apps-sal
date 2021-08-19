import math
n = int(input())
for _ in range(n):
    (a, b) = map(int, input().split())
    ans = a // math.gcd(a, b) * (b // math.gcd(a, b))
    print(ans)
