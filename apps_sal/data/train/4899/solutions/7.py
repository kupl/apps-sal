# i0 = 0.14849853757254047
import math

def weight(n, w):
    area=0
    for n in range(0,n):
        Bn=math.exp(-1-n)
        Kn=math.exp(-n)
        if(Kn<1e-300)or(Bn<1e-300):
            n+=1
        else:
            aire=0.5*(n*Bn**2-n*Kn**2+(Kn**2-Bn**2)/2+Bn**2*math.log(Bn)-Kn**2*math.log(Kn))
        area+=aire
    return area*w
