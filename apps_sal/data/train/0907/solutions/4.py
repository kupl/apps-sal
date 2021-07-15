t=int(input())
for i in range(t):
 n=int(input())
 s=input()
 c=0
 for i in s:
  if i=='H':
   c=c+1
  if i=='T':
   c=c-1
  if c>1:
   break
  if c<0:
   break
 if c==0:
  print('Valid')
 else:
  print('Invalid')# cook your dish here

