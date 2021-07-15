def ch(a,b,c,d,e,f):
 d1=abs(a-d)
 d2=abs(b-e)
 d3=abs(c-f)
 if(a+b+c==0 or d+e+f==0):
  if(d1%2==d2%2 and d2%2==d3%2):
   print(2)
  else:
   print(1)
 else:
  case=d1%2+d2%2+d3%2
  if(case%3==0):
   print(0)
  else:
   print(1)
t=int(input())
while(t):
 t-=1
 a,b,c,d,e,f=list(map(int,input().split()))
 if(a==d and b==e and c==f):
  print(0)
 else:
  ch(a,b,c,d,e,f)
 
 

