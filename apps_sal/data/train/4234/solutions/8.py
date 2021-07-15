
def num_blocks(w, l, h):
    return h*w*l + (w+l)*h*(h-1)//2 + h*(h-1)*(2*h-1)//6
