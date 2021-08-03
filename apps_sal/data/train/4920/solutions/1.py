from functools import reduce
def gcd(a, b): return a if not b else gcd(b, a % b)
def lcm(a, b): return a * b / gcd(a, b)


def min_special_mult(arr):
    errors = []
    xs = set()
    for x in [_f for _f in arr if _f]:
        try:
            xs.add(int(x))
        except:
            errors.append(x)
    if not errors:
        return reduce(lcm, xs)
    if not errors[1:]:
        return "There is 1 invalid entry: %s" % errors[0]
    return "There are %d invalid entries: %s" % (len(errors), errors)
