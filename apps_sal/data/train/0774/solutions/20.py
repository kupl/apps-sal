# cook your dish here
from sys import stdin
n,k,p=map(int,stdin.readline().split())
list1=list(map(int,stdin.readline().split()))
list2=[]
for i in range(n):
 list2.append((list1[i],i+1))
list2.sort(reverse=True)
dict1={}
dict1[list2[0][1]]=list2[0][0]+k
prev=list2[0]
for each in list2[1:]:
 if each[0]+k<prev[0]:
  dict1[each[1]]=each[0]+k
  prev=each
 else:
  dict1[each[1]]=dict1[prev[1]]
  prev=each
#print(dict1)
for j in range(p):
 a,b=map(int,stdin.readline().split())
 if dict1[a]==dict1[b]:
  print("Yes")
 else:
  print("No")
