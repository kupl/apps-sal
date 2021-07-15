from itertools import combinations

def counting_triangles(v):
    v.sort()
    return sum(a+b>c for a,b,c in combinations(v,3))
