from numpy import sin, cos, pi
def crusoe(n, d, ang, dist_mult, ang_mult):
    return (sum(d*dist_mult**i*cos(ang*ang_mult**i/180*pi) for i in range(n)), sum(d*dist_mult**i*sin(ang*ang_mult**i/180*pi) for i in range(n)))
