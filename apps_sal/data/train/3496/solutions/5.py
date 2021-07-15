def sort_by_area(seq):
    lista = list()
    for x in seq:
        if type(x) == tuple:
            area = x[0]*x[1]
        else:
            area = 3.14*x**2
        lista.append((area, x))
    return [x[1] for x in sorted(lista)]
