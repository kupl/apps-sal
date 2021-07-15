# cook your dish here
x=int(input())
for i in range(x):
 s1=str(input())
 s2=str(input())
 c=0
 for j in s1:
  for k in s2:
   if(j==k):
    c=c+1
 if(c>0):
  print('Yes')
 else:
  print('No')
