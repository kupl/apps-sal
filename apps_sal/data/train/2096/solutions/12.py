MOD = 1000000007
def ii(): return int(input())
def si(): return input()
def dgl(): return list(map(int, input()))
def f(): return map(int, input().split())
def il(): return list(map(int, input().split()))
def ls(): return list(input())


n = ii()
l = il()
l2 = sorted(l)
sd = dict((l2[i], i) for i in range(n))
ans = []
lvis = set()
for i in range(n):
    if not l[i] in lvis:
        tmp = [i + 1]
        x = sd[l[i]]
        lvis.add(l[i])
        while x != i:
            lvis.add(l[x])
            tmp.append(x + 1)
            x = sd[l[x]]
        ans.append(tmp)
print(len(ans))
for i in ans:
    print(len(i), *i)
