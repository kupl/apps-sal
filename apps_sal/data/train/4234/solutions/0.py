def num_blocks(w, l, h):
    return w*l*h + (w+l)*h*(h-1)/2 + h*(h-1)*(2*h-1)/6
