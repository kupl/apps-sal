import math
def forloop(list,list1):
 r = 1
 for x in list:
  r *= x
  for i in list1:
   if(r%i==0):
    break;
 return i
t=int(input())
while(t>0):
 l1=[]
 n=int(input())
 l=list(map(int,input().split()))
 for i in range(2,1000000):
  l1.append(i*i)
 l1=tuple(l1)
 n1=forloop(l,l1)
 ans=math.sqrt(n1)
 print(int(ans))
 t-=1
