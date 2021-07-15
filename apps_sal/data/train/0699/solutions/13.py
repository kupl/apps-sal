# cook your dish here
t=int(input())
while t>0 :
 a=list(map(int,input().rstrip().split()))
 n=a[0]
 k=a[1]
 d=a[2]
 a1=list(map(int,input().rstrip().split()))
 x=sum(a1)//k 
 if x<=d:
  print(x)
 else:
  print(d)
 t=t-1

