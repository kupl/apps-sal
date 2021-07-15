for i in range(int(input())):
 n=int(input())
 c=[int(z) for z in input().split()]
 c.sort()
 c.reverse()
 b1,b2=0,0
 for i in range(n):
  if b1<b2:
   b1+=c[i]
  elif b2<b1:
   b2+=c[i]
  else:
   b1+=c[i]
 print(max(b1,b2))
   

