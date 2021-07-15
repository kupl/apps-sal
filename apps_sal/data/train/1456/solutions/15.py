import math
def Fun(a):
 if(a==0):
  return 0
 sum_n = (a*(a+1))//2
 ini = a
 p=0
 anss = 0
 while(a>=1):
  c = (a+1)//2
  anss += c*pow(2,p)
  a= a-c
  p+=1
 dd = int(math.log2(ini))
 return (sum_n-anss-dd-1)
 
t = int(input())
while(t>0):
 arr = list(map(int,input().split()))
 l = arr[0]
 r = arr[1]
 ans = Fun(r) - Fun(l-1)
 print(ans)
 t=t-1
