# cook your dish here
from sys import stdin,stdout

for _ in range(int(input())):
 n,d=map(str,stdin.readline().split())
 li=list(n)
 s=d 
 # print(li)
 c=0
 for i in range(len(n)-1,-1,-1):
  if li[i]>d:
   li[i]=''
   c+=1 
  else:
   d=li[i]
 s=''.join(li)+c*s
 print(s)
