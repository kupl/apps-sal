n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
max1=max(a)
min1=min(a)
if k==0:
 for i in range(n):
  print(a[i], end=' ')
elif k%2==1:
 for i in range(n):
  print(max1-a[i], end=' ') 
else:
 for i in range(n):
  print(a[i]-min1, end=' ')

