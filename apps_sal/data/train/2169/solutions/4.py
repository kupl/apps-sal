from collections import defaultdict
(n, p, k) = list(map(int, input().split()))
d = defaultdict(int)
a = list(map(int, input().split()))
ans = 0
for i in a:
    b = pow(i, 4, p)
    temp = i * k % p
    fin = (b - temp) % p
    ans += d[fin]
    d[fin] += 1
print(ans)
