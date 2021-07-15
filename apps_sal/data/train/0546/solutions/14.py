import math
t = int(input())
while(t!=0):
    d = int(input())
    bounce=0
    while(d>0):
        p = int(math.log(d,2))
        d = d- (pow(2,p))
        if(d!=0):
            bounce+=1;
    print(int(bounce))
    t-=1
