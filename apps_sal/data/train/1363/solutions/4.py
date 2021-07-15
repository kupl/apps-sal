test=eval(input())


while test>0:

 test=test-1
 N, D = list(map(int, input().strip().split()))
 number=""
 for i in range(N):
  number=number+str(D)
 num=int(number)
 sq=num*num
 z=str(sq)
 l=len(z)
 
 ans=0
 for i in range (l):
  ans=ans+(int(z[i])*(23**(i)))
  ans=ans%1000000007
 print(ans)
