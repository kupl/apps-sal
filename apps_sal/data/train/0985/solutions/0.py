# coding: utf-8
# Your code here!

n=int(input())
a=[]
for i in range(n):
    x=int(input())
    a.append(x)
    
# print(a)
ans=0
m=[1]*n
for i in range(n):
    for j in range(i):
        if a[i]%a[j]==0:
            m[i]=max(m[i],m[j]+1)
            
            
            
print(max(m))
