from collections import Counter
import math
import statistics
import itertools
a,b=list(map(int,input().split()))
# b=input()
# c=[]
# for i in a:
#     c.append(int(i))
# A,B,C= map(int,input().split())
# f = list(map(int,input().split()))
#g = [list(map(lambda x: '{}'.format(x), list(input()))) for _ in range(a)]
# h = []
# for i in range(a):
#     h.append(list(map(int,input().split())))
# a = [[0] for _ in range(H)]#nizigen
lis=[input() for i in range(a)]
ra=a-1
for i in range(ra):
    for k in range(ra-i):
        if lis[k]>lis[k+1]:
            a=lis[k]
            lis[k]=lis[k+1]
            lis[k+1]=a
print(("".join(lis)))


