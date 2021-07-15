def calculate_ratio(w,h):
    if w <= 0 or h <= 0: raise ValueError
    
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    denom = gcd(w, h)
    return "{}:{}".format(w/denom, h/denom)

