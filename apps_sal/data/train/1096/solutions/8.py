# cook your dish here
n,a,b = list(map(int,input().strip().split()))
s = []
e = []
for i in range(n):
 c,d = list(map(int,input().strip().split()))
 s.append(c)
 e.append(d)
ws = list(map(int,input().strip().split()))
vs = list(map(int,input().strip().split()))
ws.sort(reverse = True)
vs.sort()
r = 1000000
for i in range( n):
 s1 = 0
 e1 = 1000000
 for j in range(a):
  if(ws[j]<=s[i]):
   s1 = ws[j]
   break
 for j in range(b):
  if(vs[j]>=e[i]):
   e1 = vs[j]
   break
 r1 = e1-s1+1 
 if(r1<r):
  r = r1
print(r)
