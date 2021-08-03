def is_triangle(a, b, c):

    if a > 0 and b > 0 and c > 0:
        reference = sorted([a, b, c])
        if reference[2] < (reference[0] + reference[1]):
            return True
        else:
            return False
    else:
        return False
