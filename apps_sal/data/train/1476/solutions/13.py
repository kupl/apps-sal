# your code goes here
from collections import Counter
def fact(num):
 factorial = 1
 for i in range(1,num + 1):
  factorial = factorial*i
 return factorial;
t=int(input())
for _ in range(t):
 done = dict()
 strr=str(input())
 ans=fact(len(strr))
 res=Counter(strr)
 for i in res:
  done[i]=0;
 l=1
 for i in res:
  if(done[i]==0):
   l=l*fact(res[i])
   done[i]=1
 ans=ans//l
 ans=ans%1000000007
 print(ans)
