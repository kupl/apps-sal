for _ in range(int(input())):
 n,k=list(map(int,input().split()))
 t1=-(-(n/2)//k)
 t2=(n/2)//k
 if not t1:t1=1
 if not t2:t2=1
 t1= int((n-k*t1)*t1)
 t2= int((n-k*t2)*t2)
 if t1<0 and t2<0:
  print(0)
 else:
  print(max(t1,t2))


