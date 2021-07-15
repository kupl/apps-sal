from math import ceil
def group_size(S,D):
    b=2*S-1
    return ceil((-b+(b**2+8*D)**0.5)/2)-1+S
