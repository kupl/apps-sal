# cook your dish here
import math
t = int(input())
for _ in range(t):
    n = int(input())
    l = []
    if n<=3:
        print(1)
        print(1,n)
    else:
        l.append([3,1,2,3])
        for i in range(4,n,2):
            l.append([2,i,i+1])
        if n%2==0:
            l.append([1,n])
        print(len(l))
        for i in l:
            print(*i)
        

