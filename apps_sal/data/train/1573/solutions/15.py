# cook your dish here
t=int(input());
for i in range(t):
 n=int(input());
 j=n-1;
 if(j%2!=0):
  print("NO");
 else:
  print("YES");
  for i in range(1,n+1):
   k=1;
   for j in range(1,n+1):
    if(i!=j):
     if(i%2!=0):
      if(k%2!=0):
       print("1",end="");
       k+=1;
      else:
       print("0",end="");
       k+=1;
     else:
      if(k%2==0):
       print("1",end="");
       k+=1;
      else:
       print("0",end="");
       k+=1;
    else:
     print("0" , end = "")
   print();
