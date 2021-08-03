from collections import defaultdict

mxn = 10**6
n = int(input())
a = list(map(int, input().split()))
d = [0] * (mxn + 2)

for i in a:
    d[i] += 1

for i in range(1 + mxn):
    q = d[i] // 2
    d[i + 1] += q
    d[i] -= 2 * q

ct = 0
for i in d:
    ct += bin(i).count("1")
print(ct)
