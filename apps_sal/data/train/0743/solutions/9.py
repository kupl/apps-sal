# cook your dish here
t=int(input())
while(t>0):
 t-=1
 n,k=map(int,input().split())
 if((n//k)%k==0):
  print("NO")
 else:
  print("YES")
