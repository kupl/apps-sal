for _ in range(int(input())):
 s=input()
 if(len(s)<4):
  print("NO")
 else:
  i=len(s)
  if(s[i-4]=='1' and s[i-3]=='0' and s[i-2]=='0' and s[i-1]=='0'):
   print("YES")
  else:
   print("NO")
