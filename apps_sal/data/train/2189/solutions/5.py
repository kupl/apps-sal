t=int(input())
for _ in range(t):
  n=int(input())
  a=list(map(int,input().split()))
  t=sum(a)
  flag=0
  for i in range(n):
    if 2*a[i]>t:
      flag=1
      break
  if t%2==1:
    flag=1
  if flag==1:
    print('T')
  else:
    print('HL')
