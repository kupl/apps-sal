from math import gcd
n = int(input())
it = list(map(int, input().split()))
q = int(input())
aa = [{} for i in range(n)]
aa[0][it[0]] = 1
for i in range(1, n):

    for j in aa[i - 1]:
        a = gcd(j, it[i])
        try:
            aa[i][a] += aa[i - 1][j]
        except:
            aa[i][a] = aa[i - 1][j]
    try:
        aa[i][it[i]] += 1
    except:
        aa[i][it[i]] = 1
ss = {}
ma = 10**6 + 1
k = -1
for i in aa:
    k += 1
    for j in i:
        if j >= ma:
            continue
        try:
            ss[j] += aa[k][j]
        except:
            ss[j] = aa[k][j]
ll = list(ss.keys())
ll.sort()
pre = [0] * (10**6 + 1)
for i in ll:
    for j in range(i, len(pre), i):
        pre[j] += ss[i]
for _ in range(q):
    k = int(input())
    print(pre[k])
