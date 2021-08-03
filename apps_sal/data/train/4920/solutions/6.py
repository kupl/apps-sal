from fractions import gcd


def min_special_mult(arr):
    def is_int(n):
        try:
            int(n)
            return True
        except:
            return False
    orig_arr = [x for x in arr if x]
    arr = [int(x) for x in orig_arr if is_int(x)]
    if len(orig_arr) - len(arr) > 0:
        freaks = [x for x in orig_arr if not is_int(x)]
        if len(freaks) > 1:
            return "There are {} invalid entries: {}".format(len(freaks), freaks)
        return "There is 1 invalid entry: {}".format(freaks[0])

    arr = [abs(x) for x in arr]
    return reduce(lambda x, y: x * y // gcd(x, y), arr)
