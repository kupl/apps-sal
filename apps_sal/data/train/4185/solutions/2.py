def sc(w, l, g):
    return int((2*w + 2*(l-2))/(1+g)) if (2*w + 2*(l-2))%(1+g) == 0 else 0
