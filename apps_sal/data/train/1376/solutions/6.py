for i in range(int(input())):
 n,k=list(map(int,input().split()))
 lis=list(map(int,input().split()))
 mylis=[]
 val=0
 total=0
 for i in range(n+1):
  mylis.append([i,lis[i]])
 #print(mylis)
 mylis=sorted(mylis, key=lambda x: x[1])
 #print(mylis)
 i=0
 j=n
 ''''
    while len(mylis)>0:
     if val==0:
      if mylis[i][1]==k:
       mylis[i][1]-=k
       print(i,k,0,0)
       mylis=mylis[i+1:]
      elif mylis[i][1]>=k:
       mylis[i][1] -= k
       print(i, k, 0, 0)
      else:
       val=mylis[i][1]
       mylis[j][1]-=val
       print()
    '''
 while total<k*n:
  if mylis[0][1] == k:
   mylis[0][1] -= k
   print(mylis[0][0], k, 0, 0)
   mylis=mylis[1:]
   total+=k
  elif mylis[0][1] > k:
   mylis[0][1] -= k
   print(mylis[0][0], k, 0, 0)
   total+=k
  else:
   val = mylis[0][1]
   print(mylis[0][0], val, mylis[-1][0], k - val)
   mylis=mylis[1:]
   mylis[-1][1] = mylis[-1][1]-(k-val)
   total+=k

  #print(total,mylis)




