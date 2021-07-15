t=int(input())
while t>0:
  t-=1
  n,p=map(int,input().split())
  l=list(map(int,input().split()))
  l.sort()
  l.reverse()
  count=0
  k=l[p-1]
  for i in range(n):
   if l[i]<k:
    break
   else:
    count+=1
  print(count)
