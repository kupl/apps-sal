def counting_triangles(V): return sum(c < a + b for a, b, c in __import__('itertools').combinations(sorted(V), 3))
