"""
Created on Mon Apr 27 21:08:53 2020

@author: pavan
"""
for _ in range(int(input())):
    N = int(input())
    ls = list(map(int, input().split()))
    types = []
    type_count = []
    for i in ls:
        if i not in types:
            types.append(i)
    types.sort()
    for j in types:
        indices = []
        for k in range(N):
            if ls[k] == j:
                if k - 1 not in indices:
                    indices.append(k)
        type_count.append(len(indices))
    print(types[type_count.index(max(type_count))])
