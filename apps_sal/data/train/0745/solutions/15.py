for _ in range(int(input())):
 n=int(input())
 a=list(map(int,input().split()))
 s=sum(a)
 a[0]=1
 for i in range(1,len(a)):
  if a[i]>a[i-1]+1:
   a[i]=a[i-1]+1
 a[n-1] = 1
 for i in range(len(a)-2,-1,-1):
  if a[i]>a[i+1]+1:
   a[i]=a[i+1]+1
 print(s-max(a)**2)
