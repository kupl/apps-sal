import math
from collections import defaultdict
n = int(input())
a = [int(i) for i in input().split()]
op = defaultdict(int)
gcd = defaultdict(int)
for i in a:
    gcd[i] += 1
s = [a[0]]
for i in range(1, n):
    for j in range(len(s)):
        s[j] = math.gcd(a[i], s[j])
        gcd[s[j]] += 1
    s.append(a[i])
for i in gcd:
    j = i
    while j < 10 ** 6 + 1:
        op[j] += gcd[i]
        j += i
q = int(input())
for _ in range(q):
    print(op[int(input())])
