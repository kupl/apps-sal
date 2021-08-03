from math import sqrt


def side_len(x, y):
    if y < x:
        return "for fuck's sake"
    mini = y - x + 1
    maxi = x + y - 1
    result = list(range(mini, maxi + 1))
    hyp = sqrt(x**2 + y**2)
    leg = sqrt(y**2 - x**2)
    if hyp.is_integer() and mini <= hyp <= maxi:
        result.remove(int(hyp))
    if leg.is_integer() and mini <= leg <= maxi:
        result.remove(int(leg))
    return result
