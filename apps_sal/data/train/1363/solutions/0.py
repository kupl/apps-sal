val = 10**9 + 7
def MOD(a,b):
 aans = a
 ans = 1
 while b>0:
  ans = (ans*aans)%val
  aans = (aans*aans)%val
  b/=2
 return ans%val
 


for i in range(eval(input())):    
 n,d= list(map(int,input().split()))
 a=int(str(d)*n)
 sqr = str(a*a)
 ans =0
 count=0
 for ii in sqr :
  ans= ans+int(ii)*23**count
  count+=1
  z=int(ii)*ans
 print(ans % (10**9+7))
 
  

