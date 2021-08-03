def counting_triangles(V): return sum(a + b > c for a, b, c in __import__('itertools').combinations(sorted(V), 3))
