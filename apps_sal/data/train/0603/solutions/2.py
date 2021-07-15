s='abcdefghijklmnopqrstuvwxyz'
for u in range(int(input())):
 n=int(input())
 r=''
 while(1):
  r=s[n::-1]+r
  if(n<26):
   break
  n-=25
 print(r)
