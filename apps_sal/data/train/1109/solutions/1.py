t=int(input());
for i in range (0,t):
 c=0;
 n=int(input());
 for j in range (1,n+1):
  if(n%j==0):
   c=c+1;
 if(c%2==0):
  print("NO\n");
 else:
  print("YES\n");
