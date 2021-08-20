MOD = 1000000007
n = int(input())
p = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]
children = [[] for x in range(n)]
for i in range(1, n):
    children[p[i - 1]].append(i)
count = [(0, 0) for i in range(n)]
for i in reversed(list(range(n))):
    prod = 1
    for ch in children[i]:
        prod *= count[ch][0] + count[ch][1]
    if x[i]:
        count[i] = (0, prod % MOD)
    else:
        tot = 0
        for ch in children[i]:
            cur = count[ch][1] * prod // (count[ch][0] + count[ch][1])
            tot += cur
        count[i] = (prod % MOD, tot % MOD)
print(count[0][1])
