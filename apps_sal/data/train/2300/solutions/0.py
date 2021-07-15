# coding: utf-8
# Your code here!
import sys
read = sys.stdin.read
readline = sys.stdin.readline

n, = list(map(int, readline().split()))
p = [-1] + [*list(map(int, readline().split()))]

MOD = 10**9+7
child = [[] for i in range(n+1)]
tot = [None for i in range(n+1)]
one = [None for i in range(n+1)]
dep = [0]*(n+1)
p2 = [1]*(n+1)
for i in range(n):
    p2[i+1] = p2[i]*2%MOD

for v in range(n,-1,-1):
    if dep[v]==0:
        tot[v] = []
        one[v] = []
    else:
        child[v].sort(key=lambda i: dep[i])
        one[v] = one[child[v][-1]]
        tot[v] = tot[child[v][-1]]
        #one_sum = [0]*(dep[v])
        #zero_sum = [0]*(dep[v])
        child[v].pop()
        if child[v]:
            zero = [p2[tot[v][j]]-one[v][j] for j in range(-len(one[child[v][-1]]),0)]
        for c in child[v]:
            for j in range(-len(one[c]),0):
                z = p2[tot[c][j]]-one[c][j]
                one[v][j] = (one[v][j]*z+zero[j]*one[c][j])%MOD
                zero[j] = zero[j]*z%MOD
                tot[v][j] += tot[c][j]

    tot[v].append(1)
    one[v].append(1)

    child[p[v]].append(v)
    dep[p[v]] = max(dep[p[v]],dep[v]+1)        

    #print(v,tot[v],one[v])
        
#print("tot",tot[0])
#print("one",one[0])

ans = 0
for i,j in zip(tot[0],one[0]):
    ans += pow(2,n+1-i,MOD)*j%MOD

print((ans%MOD))
#print(sum(tot[0]))

