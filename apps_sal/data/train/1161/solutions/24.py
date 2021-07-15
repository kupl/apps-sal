t=int(input())
for _ in range(t):
 s=input()
 if len(s)==1:
  if s[0]=='m':
   print("mongooses")
  else:
   print("snakes")
 else:
  sc=0
  mc=0
  for i in range(len(s)):
   if s[i]=='m':
    mc+=1
  s=list(s)
  n=len(s)
  for i in range(len(s)):
   if s[i]=='s':
    if i>0 and i<n-1:
     if s[i-1]!='m' and s[i+1]!='m':
      sc+=1
     elif s[i-1]=='m':
      s[i-1]='b'
     elif s[i+1]=='m':
      s[i+1]='b'
    elif i==0:
     if s[i+1]!='m':
      sc+=1
     else:
      s[i+1]='b'
    elif i==n-1:
     if s[i-1]!='m':
      sc+=1
     else:
      s[i-1]='b'
  if sc>mc:
   print("snakes")
  elif sc<mc:
   print("mongooses")
  else:
   print("tie")

