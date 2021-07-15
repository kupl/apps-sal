# cook your dish here
s=input()
s=list(s)
n,c=0,0

j=0
while(n!=1):
 j+=1
 
 p=-1
 for i in range(len(s)-2,-1,-1):
  if(j%2!=0):

   if(s[i]=='0'):
    p=i
    break
  else:
   
   if(s[i]=='1'):
    p=i
    break
   
 if(p!=-1):
  c+=1
 
 s=s[0:p+1]
 
 if(len(s)==1) or (len(s)==0):
  n=1
 
 
print(c+1)
