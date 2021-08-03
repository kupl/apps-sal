
def match(vale, g):
    va = False
    for val in g:
        if val == -vale:
            va = True
    return(va)


def solve(g):
    m = []
    for val in g:
        if match(val, g) == False:
            m.append(val)

    return m[0]
