from fractions import Fraction
def on_line(points):
    return len(set(Fraction(a[1]-b[1],a[0]-b[0]) if a[0]!=b[0] else "Invalid" for a,b in zip(points,points[1:]) if a!=b))<2
