try:
 for _ in range(int(input())):
  s=input()
  s=list(s)
  p=set(s)
  cout=0
  if(len(p)==2):
   for i in range(0,len(s)-1):
    if(s[i]==s[i+1]):
     cout=1
  else:
   cout=1
  if(cout==1):
   print("NO")
  else:
   print("YES")
except:
 pass
