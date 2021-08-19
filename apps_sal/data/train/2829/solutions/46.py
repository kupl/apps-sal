def mul(arr, h):
    return sum((pow(i, h) for i in arr))


def array_madness(a, b):
    return mul(a, 2) > mul(b, 3)
