from fractions import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def min_special_mult(arr):
    (valid, invalid) = ([], [])
    for x in filter(None, arr):
        try:
            valid.append(abs(int(x)))
        except ValueError:
            invalid.append(x)
    if len(invalid) == 1:
        return 'There is 1 invalid entry: {}'.format(invalid[0])
    elif invalid:
        return 'There are {} invalid entries: {}'.format(len(invalid), invalid)
    return reduce(lcm, valid)
