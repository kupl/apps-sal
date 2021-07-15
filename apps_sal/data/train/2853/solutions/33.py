def solve(l, i=[]):
    for x in l[::-1]:
        i=[x]*(x not in i)+i
    return i
