import math 

def strong_num(number):
    print ()
    a=list((str(number)))
    a=[int(x) for x in a ]
    
    print(a)
    t=0
    for x in a:
        print(x)
        t+=math.factorial(x)
    b=[str(x) for x in a ]
    b=''.join((b))
    if t==int(b):
        return "STRONG!!!!"
    else:
         return "Not Strong !!"

