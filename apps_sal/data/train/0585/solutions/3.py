# cook your dish here
def _gcd(a,b):
 while(b!=0):
  a,b=b,a%b
 return a
 
def __gcd(mp):
 if(len(mp)==1):
  return mp[0]
 gcd=_gcd(mp[0],mp[1])
 for i in range(2,len(mp)):
  gcd=_gcd(gcd,mp[i])
 return gcd
 
def factors(hcf):
 if(hcf==0):
  return [1]
 factor_list=[]
 for i in range(1,int(hcf**(0.5))+1):
  if(hcf%i==0):
   factor_list.append(i)
   factor_list.append(hcf//i)
 return factor_list
 
t=int(input())
for _ in range(t):
 n,m=map(int,input().split())
 mp=list(map(int,input().split()))
 hcf=0
 if(m==1):
  hcf=mp[0]
 elif(m>1):
  hcf=__gcd(mp)
 ans=0
 factor_list=factors(hcf)
 factor_list.sort(reverse=True)
 for i in factor_list:
  if i<=n:
   ans=n-i
   break
 print(ans)
