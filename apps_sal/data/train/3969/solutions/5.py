import math
def graceful_tipping(rest_bill):
    res = rest_bill * 1.15
    if res < 10:
        return math.ceil(res)
    tmp = 5 * 10.0 ** (math.ceil(math.log10(res)) - 2)
    if res % tmp > 0:
        res += (tmp - res % tmp)
    return res

