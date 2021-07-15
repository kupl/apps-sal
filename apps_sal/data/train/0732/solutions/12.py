# cook your dish here
t=int(input())
while(t>0):
 n=int(input())
 l1=[int(x) for x in input().split()]
 l2=[int(x) for x in input().split()]
 s=0
 s1=0
 s2=0
 for i in range(n):
  s1=s1+l1[i]
  s2=s2+l2[i]
  if(s1==s2 and l1[i]==l2[i]):
   s=s+l1[i]
 print(s)
 t=t-1
