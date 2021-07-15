for _ in range(int(input())):
 n,m,q = list(map(int,input().split()))
 p = []
 dic = {}
 for i in range(q):
  x,y = list(map(int,input().split()))
  p.append([x,y])
  dic[(x,y)] = 1

 cnt = 0
 #print(dic)
 for u in p:
  r1 = u[0]
  r2 = u[1]

  one = (r1-1,r2)
  two = (r1+1,r2)
  thr = (r1,r2-1)
  fo = (r1,r2+1)

  s = 0
  if one in dic:
   s = s+1

  if two in dic:
   s = s+1

  if thr in dic:
   s = s+1

  if fo in dic:
   s = s+1

  #print(s)

  re = 4-s
  cnt = cnt + re

 print(cnt)


