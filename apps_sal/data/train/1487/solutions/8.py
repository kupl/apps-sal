# cook your dish here
t = int(input())
for _ in range(t):
 n = int(input())
 a = list(map(int,input().split()))
 x = int(input())
 if n==1:
  print(1,0)
  continue
 else:
  sum1 = sum(a)
  lim = x*(int((sum1/(x+1))))
  sumt = 0
  f = -1
  c1 = 0
  while lim > sumt:
   f += 1
   sumt += a[f]
   c1 += 1
  c1 = c1-1
  #print(f,c1)
  for i in range(f,n-1):
   t1 = sum(a[:i])/x
   t2 = sum(a[i+1:])
   #print(c1,i,t1,t2)
   if t1 < t2:
    c1 += 1
   elif t1==t2:
    if i >= (n-i)-1:
     c1 += 1
    break
   else:
    break
  print(c1,n-c1)
