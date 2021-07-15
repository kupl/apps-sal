try:
 for i in range(int(input())):
  n=int(input())
  l=list(map(int,input().split()))
  x=int(input())
  i=0
  j=n-1
  bi=0
  bj=1
  count1=l[j]*x
  while(i<j):
   if(count1>0 and i!=j):
    #print(count1,i)
    if(l[i]<=count1):
     count1=count1-l[i]
     i=i+1
     bi=bi+1
    else:
     l[i]=l[i]-count1
     count1=0
   if(count1<=0):
    #print(count1,i)
    j=j-1
    count1=count1+l[j]*x
    #print(count1,i,j)
    if(i<j):
     bj=bj+1
    if(i==j):
     if(bi>bj):
      bi=bi+1
     elif(bi<bj):
      bj=bj+1
     else:
      bi=bi+1
  print(bi,bj)
except:
 pass

