from collections import Counter
(n, p, k) = map(int, input().split())
a = map(int, input().split())
ans = 0
for (k, v) in Counter([(x ** 4 - x * k) % p for x in a]).items():
    ans += v * (v - 1) >> 1
print(ans)
