def array_madness(a, b):

    def r(arr, p):
        return sum([number ** p for number in arr])
    return r(a, 2) > r(b, 3)
