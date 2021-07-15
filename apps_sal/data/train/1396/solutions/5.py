for _ in range(int(input())):
 n,m,x,y=map(int,input().split())
 n,m=n-1,m-1
 if((n%x==0 and m%y==0) or (n%x==1 and m%y==1)):
  print("Chefirnemo")
 elif((n>0 and x==1 and m%y==1) or (m>0 and y==1 and n%x==1)):
  print("Chefirnemo")
 else:
  print("Pofik")
