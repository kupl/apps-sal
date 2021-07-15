import math
import numpy as np

n,m = map(int, input().split())
hyp = math.sqrt(1+m*m)
cosx = 1/hyp
sinx = m/hyp

pts = np.array([list(map(int, input().split())) for i in range(n)]).T
    
ptsx = cosx*pts[0]+sinx*pts[1]
ptsy = cosx*pts[1]-sinx*pts[0]

w = max(ptsx)-min(ptsx)
l = max(ptsy)-min(ptsy)

print(2*l+2*w)

