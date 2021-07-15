# cook your dish here
t=int(input())
for i in range(t):
 res=0
 n=int(input())
 l1=list(map(int,input().split()))
 l1.sort()
 for i in range(n//2):
  res=res+abs(l1[i]-l1[n-i-1])
 print(res)
