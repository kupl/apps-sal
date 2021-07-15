import math

def middle_point(x1, y1, z1, x2, y2, z2, x3, y3, z3):
         
    distances = [ math.pow(x1 -x2, 2.0) + math.pow(y1 -y2, 2.0) + math.pow(z1 -z2, 2.0),  #d12
                  math.pow(x1 -x3, 2.0) + math.pow(y1 -y3, 2.0) + math.pow(z1 -z3, 2.0),  #d13
                  math.pow(x3 -x2, 2.0) + math.pow(y3 -y2, 2.0) + math.pow(z3 -z2, 2.0)]  #d23
    
    maximum = max(distances)
    index = distances.index(maximum)
    
    return 3 - index;
