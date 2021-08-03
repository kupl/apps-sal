def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a * b / gcd(a, b)


def min_special_mult(arr):
    try:
        return reduce(lcm, map(abs, map(int, filter(None, arr))))

    except:
        invalid = [i for i in arr if type(i) == str and not i.isdigit()]

        if len(invalid) == 1:
            return "There is 1 invalid entry: %s" % invalid[0]

        return "There are %s invalid entries: %s" % (len(invalid), invalid)
