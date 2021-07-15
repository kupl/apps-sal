t=int(input())
for i in range(t):
 n=int(input())
 a=[]
 c1=0
 c2=0
 for i in range(n):
  s=input()
  a.append([s[0:n//2].count("1"),s[n//2:].count("1")])
  c1+=a[i][0]
  c2+=a[i][1]
 tp1=c1
 tp2=c2
 m=abs(c1-c2)
 for i in range(n):
  tp1+=a[i][1]
  tp1-=a[i][0]
  tp2+=a[i][0]
  tp2-=a[i][1]
  if(m>abs(tp1-tp2)):
   m=abs(tp1-tp2)
  tp1=c1
  tp2=c2
 print(m)
  
  
   
  
  
  
 
 
 
  

