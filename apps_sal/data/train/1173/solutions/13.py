# cook your dish here
# cook your dish here
t=int(input())
while t>0:
 n=int(input())
 inp=[int(i) for i in input().split()]
 #print(inp)
 t=t-1
 xorarr=[0]*n
 xorarr[0]=inp[0]
 mydict=dict()
 mydict[xorarr[0]]=1
 for i in range(1,n):
  xorarr[i]=xorarr[i-1]^inp[i]
  if xorarr[i] not in mydict:
   mydict[xorarr[i]]=1
  else:
   mydict[xorarr[i]]=mydict[xorarr[i]]+1
 #print(xorarr)
 #print(mydict)
 mydicts=dict()
 sums=0
 for i in range(n):
  if xorarr[i]==0:
   sums=sums+i
   
  if xorarr[i] not in mydicts:
   val=0-i*(mydict[xorarr[i]]-1)
   mydicts[xorarr[i]]=[1,val]
   
  else:
   val=(2*mydicts[xorarr[i]][0]-mydict[xorarr[i]]+1)*i
   mydicts[xorarr[i]][0]+=1
   mydicts[xorarr[i]][1]+=val 
 #print(mydicts)
 
 for i in list(mydicts.keys()):
  sums=sums+mydicts[i][1]-(mydict[i]*(mydict[i]-1)/2)
  
 print(int(sums))
 #print(mydicts)

