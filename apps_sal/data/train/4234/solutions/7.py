def num_blocks(w, l, h):
    res= w*l*h 
    h-=1
    A = h*(h+1)//2
    B = (h+1)*(2*h+1)*h//6
    res+= (w+l)*A+B
    return res
