from fractions import Fraction

def to_string(self):
    n, d = self.numerator, self.denominator
    s, w, n = "-" if n < 0 else "", *divmod(abs(n), d)
    r = " ".join((str(w) if w else "", f"{n}/{d}" if n else "")).strip()
    return f"{s}{r}"

Fraction.__str__ = to_string
Fraction.to_decimal = lambda self: self.numerator / self.denominator
