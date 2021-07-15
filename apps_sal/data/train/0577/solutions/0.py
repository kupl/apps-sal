knows=input()
n=eval(input())
while n!=0:
 n=n-1
 word=input()
 for x in word:
  ctr=0
  for y in knows:
   if x==y:ctr=ctr+1;break
  if ctr==0:print('No');break
 else: print('Yes')
