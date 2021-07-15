a,n,k=map(int, input().split())
l=[]
for _ in range(k):
 l.append(a%(n+1))
 a//=(n+1)
print(*l)
