def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    sum = a + b + c
    if fits(sum, max(a, b, c)):
        return True
    return False


def fits(sum, a):
    return sum - a > a
