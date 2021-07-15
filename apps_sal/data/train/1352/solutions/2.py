for j in range(int(input())):
 n=int(input())
 l=list(map(int, input().split()))
 for k in range(min(l), max(l)+1):
  tmp = l.count(k)
  if tmp>0:
   print("%d: %d" % (k,tmp))
