import math as mt
sz = 1000501
n = int(input())
x = [0] * sz
gcs = [0] * int(n)
a = [int(temp) for temp in input().split()]
gcs[n - 1] = a[n - 1]
i = n - 2
while i >= 0:
    gcs[i] = mt.gcd(gcs[i + 1], a[i])
    i -= 1
i = 0
while i < n:
    curr = a[i]
    if curr < sz:
        x[curr] += 1
    j = i + 1
    while j < n:
        curr = mt.gcd(curr, a[j])
        if curr == gcs[j]:
            x[curr] += (n - j)
            break
        elif curr < sz:
            x[curr] += 1
        j += 1
    i += 1
q = int(input())
for i in range(q):
    q1 = int(input())
    ans = 0
    for t in range(1, int(mt.sqrt(q1) + 1)):
        if q1 % t == 0:
            if q1 / t == t:
                ans += x[t]
            else:
                ans += x[t]
                ans += x[int(q1 / t)]
    print(ans)
