# cook your dish here

for i in range(int(input())):
 x=int(input())
 s= input()
 s=list(s)
 if x%2 == 0:
  for i in range(0,x,2):
   s[i], s[i+1] = s[i+1],s[i]
 else:
  for i in range(0,x-1,2):
   s[i],s[i+1] = s[i+1],s[i]
 for i in range(x):
  if ord(s[i]) <= 109:
   s[i] = chr(122 - (ord(s[i])-97))
  else:
   s[i] = chr(97 + (122-ord(s[i])))
 print(''.join(s))
