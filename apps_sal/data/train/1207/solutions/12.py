try:
 t=int(input())
 for i in range(t):
  n=int(input())
  l=list(map(int,input().split()))
  l.sort()
  cost=0
  for j in range(1,len(l)):
   cost=cost+l[0]*l[j]
  print(cost)
except:
 pass
