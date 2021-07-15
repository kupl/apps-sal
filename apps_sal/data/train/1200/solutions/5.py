# cook your dish here
n=int(input())
for i in range(n):
 str1=input().strip()
 i=0
 while i<len(str1)-1:
  if str1[i]=='A' and str1[i+1]=='B' or str1[i]=='B' and str1[i+1]=='A':
   i+=2
   c=0
  else:
   c=1
   break
 if c!=0:
  print('no')
 else:
  print('yes')

