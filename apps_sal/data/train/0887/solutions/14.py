for _ in range(int(input())):
 n = int(input())
 a = [int(x) for x in input().split()]
 b = [int(x) for x in input().split()]
 flag = 1
 if a[0]!=0 or b[n-1]!=0:
  flag = 0
 if a[n-1]!=b[0]:
  flag = 0
 for i in range(1, n-1):
  if a[i]==0 or b[i]==0:
   flag = 0
  if a[i]+b[i]<b[0]:
   flag = 0
  if b[0]+a[i]<b[i]:
   flag = 0
  if b[i]+b[0]<a[i]:
   flag = 0
 if flag==1:
  print('Yes')
 else:
  print('No')

