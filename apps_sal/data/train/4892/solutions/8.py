import math

def area(x,y,z):
    a = math.hypot(x[0]-y[0],x[1]-y[1])
    b = math.hypot(x[0]-z[0],x[1]-z[1])
    c = math.hypot(z[0]-y[0],z[1]-y[1])
    p = (a+b+c)/2
    s = (p*(p-a)*(p-b)*(p-c))**.5 
    if abs(s)/(a+b+c)<1e-6: 
        return 0
    return round(s,6)


def find_biggTriang(listPoints):
    num_of_pts = len(listPoints)
    num_of_tri = 0
    best_area = None
    best_list = []
    for i in range(num_of_pts-2):
        for j in range(i+1,num_of_pts-1):
            for k in range(j+1,num_of_pts):
                a = area(listPoints[i],listPoints[j],listPoints[k])
                if a>0:
                    num_of_tri += 1
                    if best_area is None or best_area<a:
                        best_area = a
                        best_list = []
                    if a==best_area:
                        best_list.append([list(listPoints[x]) for x in (i,j,k)])
    if len(best_list)==1:
        best_list = best_list[0]
    return [num_of_pts, num_of_pts*(num_of_pts-1)*(num_of_pts-2)//6,num_of_tri,best_list,best_area]
