def invert(lst):
    def mult(n):
        return n * -1
    x = list(map(mult, lst))
    return x
