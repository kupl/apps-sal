m=pow(10,9)+7
for _ in range(int(input())):
 n=int(input())
 l=list(map(int,input().split()))
 t=1
 for i in range(n-1):
  if(l[i]<=l[i+1] and l[i]&l[i+1]==l[i]):
   y=bin(l[i]).count('1')
   t=(t*pow(2,y,m))%m
  else:
   t=0
   break
 print(t%m)
