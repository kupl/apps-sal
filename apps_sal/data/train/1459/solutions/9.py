import math


n,m = map(int, input().split())
hyp = math.sqrt(1+m*m)
cosx = 1/hyp
sinx = m/hyp

pts = [[], []]
for i in range(n):
    p = input().split()
    px = int(p[0])
    py = int(p[1])
    pts[0].append(cosx*px+sinx*py)
    pts[1].append(cosx*py-sinx*px)

w = max(pts[0])-min(pts[0])
l = max(pts[1])-min(pts[1])

print(2*l+2*w)
