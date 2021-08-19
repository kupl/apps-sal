import math
t = int(input())
for _ in range(t):
    n = int(input())
    s = int(n ** 0.5)
    cands = list(range(max(0, s - 100), s + 100))
    ans = min((x + math.ceil(n / (x + 1)) - 1 for x in cands))
    print(ans)
