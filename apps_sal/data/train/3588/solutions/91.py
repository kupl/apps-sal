def quadratic(x1, x2):
    lst = list()
    a = 1
    lst.append(a)
    b = -(x1+x2)
    lst.append(b)
    c = x1 * x2
    lst.append(c)
    tpl  = tuple(lst)
    return tpl
