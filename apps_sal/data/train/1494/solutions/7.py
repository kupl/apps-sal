from collections import defaultdict
n=int(input())
l=[]
for i in range(n):
    l.append([int(input()),0])
l.sort(key=lambda x:x[0],reverse=True)
ans=0
y=0
for i in range(n):
    if l[i][1]==1:
        continue
    for j in range(max(y,i+1),n):
        if l[j][1]==0 and 2*l[j][0]<=l[i][0]:
            l[j][1]=1
            l[i][1]=1
            ans+=1
            break
        y=j
for i in range(n):
    if l[i][1]==0:
        ans+=1
print(ans)
#print(l)


