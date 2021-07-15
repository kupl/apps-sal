from itertools   import combinations
from collections import defaultdict

def crossProd(v1, v2):   return v1[0]*v2[1] - v2[0]*v1[1]
def vectorize(pt1, pt2): return [b-a for a,b in zip(pt1, pt2)]
def notOnSameLine(*pts): return bool( crossProd(vectorize(*pts[:2]), vectorize(*pts[1:])) )

def count_col_triang(input_):
    dctPts = defaultdict(list)
    for pos,color in input_: dctPts[color].append(pos)
    
    dctTriangles = { color: sum(notOnSameLine(*threePts) for threePts in combinations(lst, 3)) for color,lst in dctPts.items() }
    maxTriangles = max(dctTriangles.values())
    
    return [len(input_),
            len(dctPts),
            sum(dctTriangles.values()),
            sorted(color for color,n in dctTriangles.items() if n == maxTriangles) + [maxTriangles] if maxTriangles else [] ]
