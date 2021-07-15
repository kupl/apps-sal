'''def pow1(ap,op):
    if op==0:
     return 1 
    elif op%2==0:
     y=pow1(ap,op/2)
     return y*y   
    else:
     y=pow1(ap,op-1)
     return ap*y '''
n=int(input())
for i in range(n):
 k,l=map(int,input().split())
 bc=l
 ans=0
 kp=1000000007
 for j in range(1,k+1):
  l=pow(bc,(2*j)-1,kp)
  ans=(l+ans)%kp
  bc=(l*bc)%kp
 print(ans)
