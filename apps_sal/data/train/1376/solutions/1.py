# cook your dish here
t=int(input())
for i in range(0,t):
 n,k=list(map(int,input().split()))
 c=list(map(int,input().split()))
 l=c[:]
 while(sum(l)!=0):
  a=max(l)
  b=min(l)
  m1=c.index(a)
  m2=c.index(b)
  n1=l.index(a)
  n2=l.index(b)
  print(str(m2)+" "+str(c[m2])+" "+str(m1)+" "+str(k-c[m2]))
  l[n1]=l[n1]-(k-c[m2])
  del l[n2]
  c[m1]=c[m1]-(k-c[m2])
  c[m2]=0 
  
   

