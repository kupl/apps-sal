from itertools import combinations, groupby, starmap

is_triangle = lambda a,b,c: (b[0]-a[0])*(c[1]-a[1]) - (c[0]-a[0])*(b[1]-a[1]) != 0
is_triangle = lambda a,b,c: a[0]*(b[1]-c[1]) + b[0]*(c[1]-a[1]) + c[0]*(a[1]-b[1]) != 0
#is_triangle = lambda a,b,c: __import__('numpy').linalg.det([(x,y,1) for x,y in (a,b,c)]) != 0 ## Precision issues

def count_col_triang(input_):
    grouped = groupby(sorted(input_, key=lambda p:p[1]), key=lambda p:p[1])
    colored_triangles = {k: sum(starmap(is_triangle, combinations((p for p, _ in g), 3))) for k, g in grouped}
    max_colored = max(colored_triangles.values())
    return [len(input_), len(colored_triangles), sum(colored_triangles.values()),
            sorted(c for c, n in colored_triangles.items() if n == max_colored) + [max_colored] if max_colored else []]
