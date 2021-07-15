def char_concat(w):
    n = len(w)//2
    return "".join(c[0]+c[1]+str(i+1) for i, c in enumerate(zip(w[:n], w[:-n-1:-1])))
