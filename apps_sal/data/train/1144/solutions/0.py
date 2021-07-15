T= int(input());

for i in range(T):
 n,k = list(map(int,input().split()));
 s=list(map(int,input()));

 if k==1:
  s_0 ={};
  s_1={};
  c0=0;
  c1=0;
  for j in range(n):
   if(j%2==0):
    s_1[j]=1;
    s_0[j]=0;
   else:
    s_1[j]=0;
    s_0[j]=1;
  for j in range(n):
   if(s_0[j]-s[j]!=0):
    c0+=1;
   if(s_1[j]-s[j]!=0):
    c1+=1;

  if c0<c1:
   print(c0);
   p_s="";
   for j in range(n):
    p_s+=str(s_0[j]);
   print(p_s);
  else:
   print(c1);
   p_s="";
   for j in range(n):
    p_s+=str(s_1[j]);
   print(p_s);

 else:
  count=1;
  c=s[0];
  flips=0
  for j in range(1,n):
   if(s[j]==c):
    count+=1;
    #print count;
    if count > k:
     if(j+1<n and s[j]==s[j+1]):
      if(s[j]==1):
       s[j]=0;
      else:
       s[j]=1;
     else:
      if(s[j-1]==1):
       s[j-1]=0;
      else:
       s[j-1]=1;
     flips+=1;
     count=1;


   elif(s[j]!=c):
    count=1;
   c=s[j];

  print(flips);
  p_s="";
  for j in range(n):
   p_s+=str(s[j]);
  print(p_s);
