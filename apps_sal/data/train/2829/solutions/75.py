def array_madness(a,b):
    r = lambda arr, p: sum([number**p for number in arr])
    return r(a,2) > r(b,3)
