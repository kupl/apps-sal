from fractions import gcd

def calculate_ratio(w,h):
    if w  == 0 or h == 0:
        raise ValueError
    factor = gcd(w, h)
    return '{}:{}'.format(w // factor, h // factor)
