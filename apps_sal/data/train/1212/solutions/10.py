T=int(input())
while(T>0):
 S=input()
 ls=[0 for i in range(26)]
 for x in S:
  ls[ord(x)-65]+=1
 n=len(S)
 c=1
 ls.sort(reverse = True)
 while(c<=26):
  if(n%c != 0):
   c=c+1
   continue
  else:
   f=n//c
   i=0
   temp_min=0
   while(i<c and i<len(ls)):
    temp_min+=min(ls[i],f)
    i=i+1
   temp_min=n-temp_min 
   if(c==1):
    minimum=temp_min
   else:
    if(minimum>temp_min):
     minimum=temp_min
  c=c+1
 print(minimum) 
 T=T-1 
