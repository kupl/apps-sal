def count_circles(list_of_circles, point, count = 0):
    return sum(1 for circle in list_of_circles if point_in(circle, point))
    
def point_in(points, point):
    helper = lambda x,y: (-1)**y*(points[(x+1)%3][(y+1)%2] - points[(x+2)%3][(y+1)%2])
    D = 2*sum(points[i][0]*helper(i,0) for i in range(3))
    U = [1.0 * sum(sum(points[i][j]**2 for j in range(2))*helper(i,k) for i in range(3))/D for k in range(2)]
    return compare(point, U, radius(points,D)) if (not invalid(points, D)) else False

compare = lambda p, U, r: ((distance(U,p) < r) or (abs(r-distance(U,p))/r < 10**-10))
distance = lambda p1, p2: ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
invalid = lambda p, D: ((D == 0) or (p[0] == p[1]) or (p[0] == p[2]) or (p[1] == p[2]))
radius = lambda p, D: distance(p[0],p[1])*distance(p[0],p[2])*distance(p[1],p[2])/abs(D)
