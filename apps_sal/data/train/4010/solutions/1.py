counting_triangles=lambda V:sum(a+b>c for a,b,c in __import__('itertools').combinations(sorted(V),3))
