#!/usr/bin/env python
# coding: utf-8

# In[1]:


N, A, B = list(map(int, input().split()))
X = list(map(int, input().split()))


# In[2]:


c = 0
for i in range(N - 1):
    dist = X[i + 1] - X[i]
    if dist * A > B:
        c += B
    else:
        c += dist * A
print(c)


# In[ ]:
