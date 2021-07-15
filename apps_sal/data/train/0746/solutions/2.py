import sys

def f(a,b,c,l,d):
 #   print a,b,c
 if a>l:
  return 1
 if b == c:
  return d[a]
 else:
  mid = (b+c)/2
  id1 = f(2*a,b,mid,l,d) 
  id2 = f(2*a+1,mid+1,c,l,d) 
  
  id1 = id1*d[a]
  id2 = id2*d[a]
  
#       print id1,id2

  if id1 > id2:
   return id1
  else:
   return id2
 

t = int(sys.stdin.readline())

while t:
 d = []
 d.append(0)
 x = sys.stdin.readline().split()
 l = len(x)
 for i in range(l):
  d.append(int(x[i]))

 ans = f(1,1,(1<<t)-1,(1<<t)-1,d)
 ans = ans % 1000000007
 print(ans)
 
 t = int(sys.stdin.readline())

