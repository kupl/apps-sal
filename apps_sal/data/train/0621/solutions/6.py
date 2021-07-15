t=eval(input())
while t:
 t-=1
 ans=[]
 n=eval(input())
 ls=input().split(' ')
 l=len(ls[0])
 for i in range(l):
  for j in range(i,l+1):
   tmp=ls[0][i:j]
#            print tmp
   flg=0
   for k in range(n):
    if ls[k].count(tmp)>0 and len(tmp)>0:
     pass
    else:
     flg=1
   if flg==0:
    ans.append(tmp)
#    print ans
 ans=sorted(ans)
 print(max(ans,key=len))

