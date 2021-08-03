from collections import Counter


def odd_one_out(stg):
    return [c for c, n in list(Counter(stg[::-1]).items()) if n % 2][::-1]
