from fractions import Fraction

def num_blocks(w,l,h):

    a = h*w*l
    b = Fraction((h-1)*(h)*(w+l),2)
    print(b)
    c = Fraction((h-1)*h*(2*h-1),6)
    print(c)
    return int(a+b+c) 
