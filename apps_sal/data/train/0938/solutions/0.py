t=int(input())
for q in range(t):
 n=int(input())
 x=list(map(int,input().split()))
 dic={}
 dic2={}
 for i in range(n):
  dic2[x[i]]=1
 #print dic2
 if len(dic2)==n:
  n+=2
  print((n*(n-1)*(n-2)*(n-3))/24)
  continue 
 counter=0
 for i in range(n-1):
  if x[i] in dic:
   dic[x[i]]+=1
  else:
   dic[x[i]]=1
  for j in range(i,n-1):
   if x[j] in dic:
    dic[x[j]]+=1
   else:
    dic[x[j]]=1
   for p in range(j+1,n):
    if x[p] in dic:
     continue;
    for q in range(p,n):
     if x[q] in dic:
      break
     counter+=1
     #print i,j,p,q
     
  dic.clear()
 print(counter)
