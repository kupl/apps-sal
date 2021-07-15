t=int(input())
A="aeiou"
B="bcdfghjklmnpqrstvwxyz"
for _ in range(t):
 s=str(input())
 c=""
 for i in range(len(s)):
  x=""
  if s[i] in A:
   x="0"
  if s[i] in B:
   x="1"
  c=c+x
  
 w=10**9
 w=w+7
 k=int(c,2)
 print(k%w)

