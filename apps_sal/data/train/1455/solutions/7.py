n=int(input())
a=list(map(int,input().split()))
m=int(input())
for i in range(0,m):
 l,r=list(map(int,input().split()))
 b=a[l-1:r]
 b.sort()
 le=len(b)
 sum=0
 for j in range(1,le):
  sum+=((b[j]-b[j-1])**2)
 
 print(sum)
