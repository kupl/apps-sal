
def num_blocks(w, l, h):
    return h*(1-3*h+2*h*h-3*l+3*h*l-3*w+3*h*w+6*l*w)//6
