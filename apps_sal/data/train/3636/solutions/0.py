from operator import lt, gt
memo = {}


def is_bouncy(s):
    return memo[s] if s in memo else memo.setdefault(s, any(map(lt, s[:-1], s[1:])) and any(map(gt, s[:-1], s[1:])))


def bouncy_ratio(percent):
    if not 0 < percent < 1:
        raise Exception('Wrong percentage: {}'.format(percent))
    (x, y) = (100, 0)
    while y < x * percent:
        (x, y) = (x + 1, y + is_bouncy(str(x + 1)))
    return x
