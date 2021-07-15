t=int(input())
while(t>0):
 n=int(input())
 tcase=input().split(' ')
 ans=''
 alen=0
 for i in range(len(tcase[0])+1):
  for j in range(i+1):
   if all(tcase[0][j:i] in b for b in tcase):
    if(len(tcase[0][j:i])>alen):
     ans=tcase[0][j:i]
     alen=len(ans)
    elif len(tcase[0][j:i])==alen:
     if tcase[0][j:i]<ans:
      ans=tcase[0][j:i]
 print(ans)
 t=t-1 


