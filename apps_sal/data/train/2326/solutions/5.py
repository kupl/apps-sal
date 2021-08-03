from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))

G = defaultdict(list)
D = {}

for i in range(N):
    tmp = A[i]
    G[tmp].append(i)

keylist = []

for key in G:
    G[key].sort()
    D[key] = len(G[key])
    keylist.append(key)

keylist.sort()
keylist = keylist[::-1]
keylist.append(0)

D[0] = 0
G[0].append(0)

ans = [0] * N

for i in range(len(keylist) - 1):
    key = keylist[i]
    nextkey = keylist[i + 1]
    tmpi = G[key][0]
    ans[tmpi] += D[key] * (key - nextkey)

    D[nextkey] += D[key]
    G[nextkey][0] = min(G[nextkey][0], tmpi)

for i in ans:
    print(i)
