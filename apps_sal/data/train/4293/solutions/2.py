epley     = lambda w,r: w * (1+r/30)
mcGlothin = lambda w,r: 100*w / (101.3 - 2.67123*r)
lombardi  = lambda w,r: w * r**0.10

def calculate_1RM(w, r):
    return r and (w if r == 1 else round(max(epley(w,r), mcGlothin(w,r), lombardi(w,r))))
