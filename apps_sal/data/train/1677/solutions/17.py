# cook your dish here
import sys
from itertools import accumulate
read = sys.stdin.readline
n = int(read())
a = tuple(map(int , read().split()))
b = tuple(accumulate(map(int , read().split())))
#print(b)
maxs = 0
#sumb = sum(b)
for i in range(0,len(a)):
    for j in range(0,len(a)):
        t = 0
        #print(i,j)
        if(i != j):
            t += a[i]
            t += a[j]
            k = i
            l = j
            if(i < j):
                t += (b[j-1] - b[i])
                #print(i,j,t)
                #print("i<j",t)
            elif(i > j):
                if(j > 0):
                    t += (b[-1]-b[i]+b[j-1])
                #print("i>j",t)
                else:
                    t += (b[-1]-b[i])
            else:
                pass
        else:
            t = a[i]
        if(maxs < t):
            maxs = t
            #print(maxs,i,j)
print(maxs)
        
