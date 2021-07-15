import math


def splitnumber(x):
    counter =0
    while x%2 ==0:
        counter +=1
        x = x/2
    return [counter ,x]
        
   

def sharkovsky(a, b):
    x = splitnumber(a)
    y = splitnumber(b)
    
    if (x[1] ==1) and (y[1]==1):
        return a>b
    elif (x[1]!= 1) and (y[1]==1):
        return True
    elif (x[1]==1) and (y[1]!=1):
        return False
    else:
        if x[0] ==y[0]:
            return a<b
        else:
            return x[0] < y[0]

    return False

