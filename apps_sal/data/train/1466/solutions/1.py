# cook your dish here
n,k=list(map(int,input().split()))
d=[0]+list(map(int,input().split()))
l=[0]
for i in range(1,n+1):
 l.append(l[i-1]^d[i])
for q in range(k):
 x=int(input())
 print(l[x%(n+1)])

