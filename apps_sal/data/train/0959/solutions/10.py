t=int(input())
for _ in range(t):
 n=int(input())
 a=list(map(int,input().split()))
 a.sort()
 
 sum1=0
 for k in range(n//2):
  sum1=sum1+abs(a[n-k-1]-a[k])
  
 print(sum1)
