#!/usr/bin/env python
# coding: utf-8

# In[5]:


from collections import deque

stack=deque()
n=int(input())
a=list(map(int,input().split()))
res1=0
l=0

for i in a:
    while stack and stack[-1]<i:
        stack.pop()
        l-=1
        
    stack.append(i)
    l+=1
    
    if l>1:
        res1=max(res1,stack[-1]^stack[-2])
        
        
stack.clear()
l=0
res2=0
a.reverse()

for i in a:
    while stack and stack[-1]<i:
        stack.pop()
        l-=1
        
    stack.append(i)
    l+=1
    
    if l>1:
        res2=max(res2,stack[-1]^stack[-2])
        

        
print(max(res1,res2))


# In[ ]:





