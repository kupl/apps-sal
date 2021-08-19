import sys
input = sys.stdin.readline
n = int(input())
b = list(map(int, input().split()))
bb = sorted(b)
c = {bb[i]: i for i in range(n)}
a = [c[b[i]] for i in range(n)]
vis = [0] * n
out = []
for i in range(n):
    if vis[i]:
        continue
    vis[i] = 1
    newlist = [i]
    while a[newlist[-1]] != i:
        newlist.append(a[newlist[-1]])
        vis[newlist[-1]] = 1
    out.append(newlist)
print(len(out))
for i in out:
    print(' '.join([str(x + 1) for x in [len(i) - 1] + i]))
