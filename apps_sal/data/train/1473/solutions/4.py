def cut2(x, y, m, n):
 #print "got {}*{} and {},{}".format(x,y,m,n)
 return m%x==0 or n%y==0
 
def cut1(x, y, l, m, n):
 if x*y != l+m+n:
  return False
 else:
  if l%x==0:
   if cut2(x, y-l/x, m, n):
    return True
  if l%y==0:
   if cut2(x-l/y, y, m, n):
    return True
  if m%x==0:
   if cut2(x, y-m/x, l, n):
    return True
  if not m%y:
   if cut2(x-m/y, y, l, n):
    return True
  if not n%x:
   if cut2(x, y-n/x, m, l):
    return True
  if not n%y:
   if cut2(x-n/y, y, m, l):
    return True
  return False

t = int(input())

for i in range(t):
 x, y, l, m, n = list(map(int, input().strip().split()))
 print("Yes" if cut1(x,y,l,m,n) else "No")

