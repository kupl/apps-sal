t=eval(input())
for ii in range(t):
 s=input()
 ans=0
 for i in s:
  if i.isdigit():ans+=int(i)
 print(ans)
