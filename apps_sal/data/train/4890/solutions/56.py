from functools import reduce


def find_difference(a, b):
    from functools import reduce

    def vol(_):
        return reduce(lambda x, y: x * y, _)
    return abs(vol(a) - vol(b))
