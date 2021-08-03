def f(t, r=2): return [sorted, iter][r - 2](abs(sum(p) - 2 * p[-1])**2for p in map([list, f][r - 2], __import__('itertools').combinations(t, r)))
def count_rect_triang(p): return sum(d < 1e-9for d in f({x + 1j * y for x, y in p}, 3))
