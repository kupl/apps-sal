tb=str(input())
tb=list(tb)
if("c" in tb or "k" in tb):
 print(0)
else:
 ans=1
 i=0
 while(i<len(tb)):
  if(tb[i]=="g" or tb[i]=="f"):
   my=tb[i]
   i+=1
   ct=1
   while(i<len(tb) and tb[i]==my):
    ct+=1
    i+=1
   if(ct>3):
    ct+=1
   ans*=ct
  else:
   i+=1
 print(ans)
