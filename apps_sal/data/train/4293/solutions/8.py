def calculate_1RM(w, r):
    if r == 0:
        return 0
    if r == 1:
        return w
    return max(int(round(w*(1+r/30))),int(round(100*w/(101.3-2.67123*r))),int(round(w*r**(1/10))))
