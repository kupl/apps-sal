import math
import numpy as np


n,m = map(int, input().split())
hyp = math.sqrt(1+m*m)
cosx = 1/hyp
sinx = m/hyp

px = np.empty(n)
py = np.empty(n)
for i in range(n):
    p = input().split()
    px[i] = int(p[0])
    py[i] = int(p[1])

w = max(cosx*px+sinx*py)-min(cosx*px+sinx*py)
l = max(cosx*py-sinx*px)-min(cosx*py-sinx*px)

print(2*l+2*w)

