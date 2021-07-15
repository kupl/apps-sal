from sys import *
input=stdin.readline
l=[0]*(10**6+1)
l[1]=1
p=1
m=10**9+7
for i in range(2,10**6+1):
 l[i]=(l[i-1]*(p*i)%m)%m
 p*=i
 p=p%m
for u in range(int(input())):
 print(l[int(input())])

