for _ in range(int(input())):
 n=int(input())
 a=[]
 g=[]
 h=[]
 I=list(map(int,input().split()))
 P=list(map(int,input().split()))
 a.append(I[0])
 a.append(P[0])
 h.append(I[1])
 h.append(P[1])
 g.append(a[1]-a[0])
 for i in range(2,n):
  L=list(map(int,input().split()))
  a.append(L[0])
  g.append(a[i]-a[i-2])
  h.append(L[1])
 g.append(a[-1]-a[-2])
 g.sort()
 h.sort()
 var=0
 for i in range(n):
  var+=h[i]*g[i]
 print(var)
  
  
 

