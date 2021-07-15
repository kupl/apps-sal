from math import floor,ceil
for _ in range(int(input())):
 n,k=map(int,input().split())
 t1=ceil(ceil(n/2)/k)
 t2=ceil(floor(n/2)/k)
 t3=floor(ceil(n/2)/k)
 t4=floor(floor(n/2)/k)
 if not t1:t1=1
 if not t2:t2=1
 if not t3:t3=1
 if not t4:t4=1
 t1= int((n-k*t1)*t1)
 t2= int((n-k*t2)*t2)
 t3= int((n-k*t3)*t3)
 t4= int((n-k*t4)*t4)
 if t1<0 and t2<0 and t3<0 and t4<0:
  print(0)
 else:
  print(max(t1,t2,t3,t4))
