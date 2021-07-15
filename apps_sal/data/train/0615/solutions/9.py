T = int(input())
for i in range(T):
 a = input().split(" ")
 N = int(a[0])
 Q = int(a[1])
 if(N>=1 and N<=100000 and Q>=1 and Q<=100000):
  b = input().split(" ")
  l = list(map(int,b))
  l1 = []
  for k in range(Q):
   q = input().split(" ")
   l1.extend(q)
     
  l2 = list(map(int,l1))
  m = 0
  while(m<len(l2)-1):
   s = 0
   c = l2[m]
   d = l2[m+1]
   for t in range(c-1,d):
    s = s + l[t] 
   print(s)
   m = m+2

