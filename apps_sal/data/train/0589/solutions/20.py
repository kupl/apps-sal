t=int(input())
for i in range(t):
 s=list(input())
 mx=0
 count=0
 c=0
 for j in range(len(s)):
  if s[j]=='.':
   count+=1
  else:
   if count>mx:
    c+=1
   mx=max(mx,count)
   count=0
 print(c)

