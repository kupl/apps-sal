# Monotone chain method

def cross(a,b,o):
    return (a[0]-o[0]) * (b[1]-o[1]) - (b[0]-o[0]) * (a[1]-o[1])

def hull(pts):
    q = []
    for p in pts:
        while len(q) > 1 and cross(q[-2], q[-1], p) <= 0: q.pop()
        q.append(p)
    q.pop()
    return q

def convex_hull_area(points):
    if len(points) < 3: return 0
    points = sorted(points)
    hl = hull(points) + hull(points[::-1])
    hl.append(hl[0])
    return round(sum(x1*y2 - y1*x2 for (x1,y1),(x2,y2) in zip(hl, hl[1:])) / 2, 2)
