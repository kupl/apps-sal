from math import sqrt as S 
for _ in range(int(input())):
 n=int(input())
 a1=int(S(n))
 a2=n//a1
 #print(a1,a2)
 rem=n-a1*a2 
 # print(rem)
 ans=['X']*a1+['D']*a2
 if rem:
  ans.insert(-rem,'X')
 print(*ans,sep='')
