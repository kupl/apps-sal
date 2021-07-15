from math import gcd

def calculate_ratio(w, h):
    if w <= 0 or h <= 0:
        raise ValueError("Width and height should be > 0")
    d = gcd(w, h)
    return f"{w//d}:{h//d}"
