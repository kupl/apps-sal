t=int(input())
i=0
while i<t:
 n,d=input().split()
 n=int(n)
 d=int(d)
 a=[]
 days=0
 a=input().split()
 j=0
 risk=0
 while j<n:
  x=int(a[j])
  if x>=80 or x<=9:
   risk+=1
  j+=1
 nrisk=n-risk
 if risk%d==0:
  days=int(risk/d)
 else:
  days=int(risk//d)+1
 if nrisk%d==0:
  days+=int(nrisk/d)
 else:
  days+=int(nrisk//d)+1
 print(days)
 i+=1
