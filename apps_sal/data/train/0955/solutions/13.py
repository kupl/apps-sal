from collections import defaultdict
n = 10002
prime = [1] * n
prime[0] = 0
prime[1] = 0
primelist = []
pairs = defaultdict(list)
for i in range(2, n):
    if prime[i] == 1:
        primelist.append(i)
        for j in range(i * i, n, i):
            prime[j] = 0
d = defaultdict(int)
for p in primelist:
    for q in primelist:
        d[p + 2 * q] += 1
        pairs[p + 2 * q].append((p, q))
t = int(input())
while t:
    t -= 1
    num = int(input())
    print(d[num])
