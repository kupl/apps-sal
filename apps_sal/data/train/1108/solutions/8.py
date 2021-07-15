# cook your dish here
n,m,k=map(int,input().split())
co=0
for i in range(n):
 l=list(map(int,input().split()))
 s=0
 for j in range(k):
  s=s+l[j]
 if s>=m and l[k]<=10:
  co=co+1
print(co)
