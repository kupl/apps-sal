for i in range(int(input())):
 a,b=list(map(int,input().split()))
 y=list(map(int,input().split()))
 s=0
 if y[0]>b:
  s+=y[0]//b
  if y[0]%b==0:
   s-=1
 for j in range(1,a):
  diff=y[j]-y[j-1]
  s+=(diff//b)
  if diff%b==0:
   s-=1
 print(s)
