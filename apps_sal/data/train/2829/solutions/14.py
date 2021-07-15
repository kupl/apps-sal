from functools import reduce
def array_madness(*arrays):
    return int.__gt__(*[reduce(lambda a,c:a+c**(2+i), a, 0) for i,a in enumerate(arrays)])

