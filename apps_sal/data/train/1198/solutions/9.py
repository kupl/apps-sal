import math
from collections import defaultdict
n = int(input())
a = [int(i) for i in input().split()]
q = int(input())
k = [int(input()) for i in range(q)]
K = max(k)
op = defaultdict(int)
gcd = defaultdict(int)
smallestgcd = a[0]
for i in a:
    gcd[i] += 1
    smallestgcd = math.gcd(smallestgcd, i)
s = [a[0]]
for i in range(1, n):
    for j in range(len(s)):
        if s[j] != 1 and s[j] != smallestgcd:
            s[j] = math.gcd(a[i], s[j])
        gcd[s[j]] += 1
    s.append(a[i])
if gcd[1] != 0:
    op = defaultdict(lambda: gcd[1])
for i in gcd:
    j = i
    if j == 1:
        continue
    while j < K + 1:
        op[j] += gcd[i]
        j += i
for z in range(q):
    print(op[k[z]])
