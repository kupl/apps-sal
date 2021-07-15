import sys
input = sys.stdin.readline

#l = list(map(int, input().split()))
#import numpy as np
#arr = np.array([int(i) for i in input().split()])
'''
a,b=[],[]
for i in range():
    A, B = map(int, input().split())
    a.append(A)   
    b.append(B)'''

n=int(input())
a=list(map(int,input().split()))
x=0
for item in a:
    x^=item
ans=[]
for item in a:
    ans.append(x^item)
ans=map(str,ans)
print(" ".join(ans))
