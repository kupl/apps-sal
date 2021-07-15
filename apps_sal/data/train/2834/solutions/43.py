def symmetric_point(p, q):

    distance = []
    for a, b in zip(p, q):
        if a > 0 and b > 0:
            distance.append(abs(a-b))
        elif a < 0 and b < 0:
            distance.append(abs(abs(a)-abs(b)))
        else:
            distance.append(abs(a)+abs(b))
            
    final_point = []
    for i, c, d in zip([0, 1],q, distance):
        if p[i] > 0 and q[i] > 0 or p[i] < 0 and q[i] < 0:
             if abs(p[i]) < abs(q[i]):
                 final_point.append(abs(c)+d)               
             else:
                 final_point.append(abs(c)-d)
        else:
           final_point.append(abs(c)+abs(d))
            
        
    return [x * -1 if q[i] < 0 else x for i, x in enumerate(final_point)]

