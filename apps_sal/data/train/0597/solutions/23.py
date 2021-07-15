t=int(input())
while t:
 dd=[]
 l=[]
 h=[]
 pr=0
 d=[]
 n=int(input())
 for i in range(n):
  x,hi=map(int,input().split())
  l.append(x)
  h.append(hi)
 l.sort()
 for i in range(1,n):
  dd.append(l[i]-l[i-1])
 d.append(dd[0])
 for i in range(1,n-1):
  d.append(dd[i]+dd[i-1])
 d.append(dd[-1])
 d.sort()
 h.sort()
 pr=0
 #print(d,h)
 for i in range(n):
  pr+=d[i]*h[i]
 print(pr)
 t-=1
