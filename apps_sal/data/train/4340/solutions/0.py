def shortest_time(speed):
    a,b,c,d = sorted(speed)
    return a+b+d + min(2*b, a+c)
