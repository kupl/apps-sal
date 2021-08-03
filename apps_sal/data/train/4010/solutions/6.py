def counting_triangles(v): return len([x for x in list(__import__('itertools').combinations(v, 3)) if all([k < sum(x) - k for k in x])])
