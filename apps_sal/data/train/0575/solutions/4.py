t=int(input())
for z in range(t):
 s=input()
 j=1
 ans=1
 a=[]
 for i in s:
  if i!='=':
   a.append(i)
 if len(a)== 0 :
  print(1)
  continue
 for i in range(len(a)-1):
  if a[i]==a[i+1]:
   j+=1
   ans=max(ans,j)
  else:
   j=1
 print(ans+1)

