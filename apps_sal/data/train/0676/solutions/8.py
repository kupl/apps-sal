# cook your dish here
from collections import Counter

T = int(input())

for _ in range(T):
    n = int(input())
    
    lists = list(map(str,input().split()))
    d = dict(Counter(lists))
    
    l = list(d.values())
    maxi = max(l)
    
    greatest = []
    for ele in d:
        if d[ele] == maxi:
            greatest.append(ele)
            
    greatest.sort()
    print(greatest[0])
   

