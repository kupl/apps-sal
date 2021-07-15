from math import pi as PI

def circle(r):         return r*r*PI
def rect(a,b):         return a*b
def getArea(r):        return rect(*r) if isinstance(r,tuple) else circle(r)
def sort_by_area(seq): return sorted(seq, key=getArea)
