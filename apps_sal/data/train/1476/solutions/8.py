import math
t=int(input())
#print(math.factorial(5))
for i in range(t):
 s=input()
 l=list(s)
 seti=set(l)
 deno=1
 for i in seti:
  deno*=(math.factorial(l.count(i)))
 leng=len(l)
 ans=((math.factorial(leng))//deno)%1000000007
 print(int(ans))
