from math import pi,cos
def spider_to_fly(spider, fly):
    a=int(spider[1])
    b=int(fly[1])
    return (a*a+b*b-2*a*b*cos((ord(spider[0])-ord(fly[0]))/4*pi))**(0.5)

