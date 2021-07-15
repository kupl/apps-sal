from fractions import Fraction

def calculate_ratio(w, h):
    if w * h == 0:
        raise ValueError
    f = Fraction(w, h)
    return f"{f.numerator}:{f.denominator}"

