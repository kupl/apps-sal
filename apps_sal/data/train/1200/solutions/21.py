# cook your dish here
t=int(input())
for ts in range(t):
 n=input()
 c=0
 for i in range(0,len(n)-1,2):
  if ((n[i]=='A' and n[i+1]=='B') or (n[i]=='B' and n[i+1]=='A')):
   c+=1
 if(c==len(n)//2):
  print('yes')
 else:
  print('no')
