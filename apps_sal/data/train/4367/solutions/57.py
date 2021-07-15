def area_or_perimeter(l , w):
    print(l,w)
    if l == w:
        return 0.5*((l*4) * (w/2))
    else:
        return (l + w) * 2
