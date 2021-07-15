# cook your dish here
def check(s,n):
 temp=0
 haha=s[0]
 for i in range(1,n):
  if(haha==s[i]):
   temp+=1
  else:
   haha=s[i]
 return temp
for _ in range(int(input())):
 s=input()
 n=len(s)
 ans=0
 for i in range(n):
  for j in range(i,n):
   temp=s[0:i]
   for t in range(i,j+1):
    if(s[t]=='0'):
     temp+='1'
    else:
     temp+='0'
   temp+=s[j+1:]
   ans+=check(temp,n)
 print(ans)
