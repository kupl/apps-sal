import math

def get_center_radius(points):
    x = [pt[0] for pt in points]
    y = [pt[1] for pt in points]
    A = x[0]*(y[1]-y[2]) - y[0]*(x[1]-x[2]) + x[1]*y[2] - x[2]*y[1]
    B = (x[0]**2 + y[0]**2)*(y[2]-y[1]) + (x[1]**2 + y[1]**2)*(y[0]-y[2]) + (x[2]**2 + y[2]**2)*(y[1]-y[0])
    C = (x[0]**2 + y[0]**2)*(x[1]-x[2]) + (x[1]**2 + y[1]**2)*(x[2]-x[0]) + (x[2]**2 + y[2]**2)*(x[0]-x[1])
    D = (x[0]**2 + y[0]**2)*(x[2]*y[1]-x[1]*y[2]) + (x[1]**2 + y[1]**2)*(x[0]*y[2]-x[2]*y[0]) + (x[2]**2 + y[2]**2)*(x[1]*y[0]-x[0]*y[1])
    return -B/(2*A), -C/(2*A), ((B**2+C**2-4*A*D)/(4*A**2))**.5

def count_circles(list_of_circles, point):
    counter = 0
    for circle in list_of_circles:
        xc, yc, r = get_center_radius(circle)
        d = math.hypot(xc - point[0], yc - point[1])
        counter += 1 if d < r or abs(d-r)/r < 10**-10 else 0

    return counter
