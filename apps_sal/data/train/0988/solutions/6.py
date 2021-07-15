# cook your dish here
from math import log2
t=int(input())
def odd(a,n):
 count=0
 for i in range(n):
  count+=a[i]%2
 if count>=n/2:
  return 1;
 return 0
def divide(a):
 for i in range(len(a)):
  a[i]=a[i]>>1
 return a;
for _ in range(t):
 n=int(input())
 a=list(map(int,input().split()))
 m=a[:]
 time=int(log2(max(a))+1)
 
 i=0
 answer=0
 while i<time:
  answer+=odd(a,n)*(1<<i)
  a=divide(a)
  i+=1
  
 x=answer;
 # print(x)
 for i in range(n):
  m[i]=m[i]^x
 # print(a)
 print(sum(m)) 

