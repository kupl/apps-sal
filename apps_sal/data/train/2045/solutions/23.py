import sys

I = lambda: int(input())
readline = lambda: sys.stdin.readline().strip('\n')
RM = readmap  = lambda x=int: list(map(x,readline().split(' ')))

n,m = RM()
conq = ['0']*(n+1)
nxt = list(range(1,n+2))#contains the nxt person alive for each person
for _ in range(m):
    l,r,m = RM()
    cur = l
    while cur<=r:
        if conq[cur]=='0' and cur!=m:   conq[cur]=str(m)
        nx = nxt[cur]
        nxt[cur] = [r+1,m][cur<m]#right most of the segment or the conqueror
        cur = nx

print(' '.join(conq[1:]))

