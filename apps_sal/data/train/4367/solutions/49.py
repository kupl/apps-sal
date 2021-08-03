def area_or_perimeter(l, w):
    def a(l, w): return l * w if(l == w) else 2 * l + 2 * w
    return a(l, w)
