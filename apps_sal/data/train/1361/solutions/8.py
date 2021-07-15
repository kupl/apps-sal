from itertools import *

try:
    x,y = map(int, input().split())
    l1=list (map(int,input().split()))


    for j in range (0,y):
        l1=list(accumulate(l1))

    for i in range(0,len(l1)):
        print(l1[i]%(pow(10,9)+7),end=' ')
except:
    pass

