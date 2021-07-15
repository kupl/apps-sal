def crusoe(n, d, ang, dis_tmult, ang_mult):
    # your code
    from math import sin,cos,pi
    
    x=0
    y=0
    for i in range(n):
        x=x+(d*dis_tmult**i)*cos(ang*pi/180*ang_mult**i)
        y=y+(d*dis_tmult**i)*sin(ang*pi/180*ang_mult**i)
    return (x,y)
