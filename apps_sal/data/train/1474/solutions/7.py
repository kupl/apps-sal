__author__ = 'ravi'
for i in range(int(input())):
 p=int(input())
 n=input().split()
 c=input()
 mx=0
 for j in range(p):
  if(mx<n[j].count(c)):
   mx=n[j].count(c)
 for k in n:
  if(mx==k.count(c)):
   print(k)
   break;

