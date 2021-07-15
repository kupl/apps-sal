""" My template """
# x0,y0,ax,ay,bx,by = list(map(int,input().split()))
# xs,ys,t = list(map(int,input().split()))
# V = []
# for i in range(61):
#     V.append([x0,y0])
#     x0=ax*x0+bx;y0=ay*y0+by;
# A=0
# for i in range(61):
#     for j in range(i,61):
#         ans=min(abs(xs-V[i][0])+abs(ys-V[i][1]),abs(xs-V[j][0])+abs(ys-V[j][1]))
#         for k in range(i,j):
#             ans=ans+abs(V[k+1][0]-V[k][0])+abs(V[k+1][1]-V[k][1])
#         if ans<=t:
#             A=max(A,j-i+1);
# print(A)

# def f(s):
#     s = str(s)
#     ans = 0
#     for i in s:
#         ans += int(i)
#     return ans

import math
import itertools
n, L, R, Ql, Qr = list(map(int, input().split()))
w = list(map(int, input().split()))
pw = list(itertools.accumulate(w))
ts = sum(w)
ans = math.inf
for i in range(n+1):
    l = i
    r = n - i
    if l > 0:
        lsum = pw[i-1]
    else:
        lsum = 0
    rsum = ts - lsum
    if l < r:
        ans = min(ans, L*lsum + rsum*R + max((r-l-1)*Qr, 0))
    else:
        ans = min(ans, L*lsum + rsum*R + max((l-r-1)*Ql, 0))
print(ans)

