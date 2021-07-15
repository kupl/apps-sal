n,q = map(int,input().split())
f = list(map(int,input().split()))
l = [0,f[0]]
for i in range(1,n,1):
 l.append(l[-1]^f[i])
l.append(0)
for _ in range(q):
 a = int(input())
 print(l[a%(n+1)])
