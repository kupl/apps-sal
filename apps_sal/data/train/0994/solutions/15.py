try:
 import math
 from sys import stdin
 from collections import defaultdict
 for _ in range(int(stdin.readline())):
  n,x=list(map(int,stdin.readline().strip().split()))
  list1=list(map(int,stdin.readline().strip().split()))
  ll=set()
  for i in range(1,n):
   list1[i]=list1[i]+list1[i-1]
  c=0 
  for i in range(1,n+1):
   if(x%i==0):
    a=i
    y=x//a
    list2=[]
    j=-1
    dict1={}
    for i in range(a-1,n):
     if(j==-1):
      list2.append(list1[i])
      if(list1[i] in dict1):
       dict1[list1[i]]+=1
      else:
       dict1[list1[i]]=1
      j+=1
     else:
      list2.append(list1[i]-list1[j])
      if(list1[i]-list1[j] in dict1):
       dict1[list1[i]-list1[j]]+=1
      else:
        dict1[list1[i]-list1[j]]=1
      j+=1
    # print(list2)
    # print(dict1)
    for k in list2:
     # dict1[k]-=1
     if(y-k in dict1):
      c+=dict1[y-k]
    # c+=dict1(y-k)
    # dict1[k]+=1
  print(c)

except:
 pass
   

