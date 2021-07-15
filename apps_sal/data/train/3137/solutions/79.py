def round_it(n):
    l, r = [len(str(i)) for i in str(n).split('.')]
    if l>r : return round(n-0.5)
    if l<r : return round(n+0.5)
    return round(n)
