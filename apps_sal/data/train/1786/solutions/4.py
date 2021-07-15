def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        
def convex_hull_area(points):
    points = sorted(points)
    
    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    hull = lower[:-1] + upper[:-1]
    
    area = 0
    n = len(hull)
    j = n - 1
    for i in range(0,n): 
        area += (hull[j][0] + hull[i][0]) * (hull[i][1] - hull[j][1]) 
        j = i 
    return round(area/2.0,2)

