from itertools import combinations as combos

def count_col_triang(in_):
    cl = list(set([i[1] for i in in_])) # cl is the full color-list
    
    d = {} # dictionary of color keys and triangle-count values
    for c in cl: # i[0] + [1] is a row of the test matrix: [xi, yi, 1]
        triples = combos([i[0] + [1] for i in in_ if i[1] == c], 3)
        test_matrices = list(map(list, triples))
        d[c] = len([i for i in test_matrices if determinant(i)])
        
    mc = max(d, key=d.get) # maximally-triangled color
    maxcl = sorted([c for c in cl if d[c] and d[c] == d[mc]])
    sumtri = sum([d[i] for i in d])
    return [len(in_), len(cl), sumtri, maxcl + [d[mc]] if sumtri else []]

def determinant(m):
    a, b, c, d, e, f, g, h, i = tuple(m[0] + m[1] + m[2])
    return a*(e*i-f*h) - b*(d*i-f*g) + c*(d*h - e*g)
