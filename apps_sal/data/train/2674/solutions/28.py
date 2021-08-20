def two_sort(a):
    a.sort()
    a = a[0]
    b = ''
    for x in a:
        b = f'{b}{x}***'
    return b[:-3]
