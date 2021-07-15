import sys
t = int(sys.stdin.readline().strip())
c=[]
for i in range(t):
 c+=[int(sys.stdin.readline().strip())]

def check(s):
 if s==1:
  return "1"
 m = int(((s-1)/2.0)+0.6)
 st=""
 for i in range(m,m+s):
  st=st+"  "+str(i)
 return st[2:]

for h in c:
 print(check(h))
