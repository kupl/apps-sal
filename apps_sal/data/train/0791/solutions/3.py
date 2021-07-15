T=int(input())
for i in range(0,T):
 (N,D)=input().split()
 N=int(N)
 D=int(D)
 L=[int(i) for i in input().split()]
 A=0
 flag=''
 MOVE=0
 s=0
 s=sum(L)
 if (s%len(L))!=0:
  print(-1)
  flag=False
 else:
  A=s/len(L)
  for i in range(N):
   if L[i]>A and (i+D)<N:
    diff=L[i]-A
    L[i]=L[i]-diff
    L[i+D]=L[i+D]+diff
    MOVE=MOVE+diff
    
   elif L[i]<A and (i+D)<N:
    diff=A-L[i]
    #if L[i+D]>=diff:
    L[i]=L[i]+diff
    L[i+D]=L[i+D]-diff
    MOVE=MOVE+diff
  for i in L:
   if i!=A and flag!=False:
    print(-1)
    flag=False
    break 
  if flag!=False:
   print(int(MOVE))
 

   
     

