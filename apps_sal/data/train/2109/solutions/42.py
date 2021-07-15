# coding: utf-8
# Your code here!
import math
Q=int(input())
for _ in range(Q):
    A,B = list(map(int,input().split()))
    if A<B:
        A,B=B,A
    S=A*B
    a=math.floor(math.sqrt(S-1))
    if a*a>S-1:
        a-=1
#    print(math.sqrt(A*B-1))
#    print('a A B',a,A,B)
    if A-B<=1:
        print((2*(B-1)))
    elif a*(a+1) < S:
        print(((B-1)+a+max(0,a-B)))
    else:
        print(((B-1)+a+max(0,a-B-1)))





