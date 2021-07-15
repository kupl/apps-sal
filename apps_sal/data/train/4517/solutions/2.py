from collections import Counter

def odd_one_out(s):
    return [k for k, v in Counter(s[::-1]).items() if v % 2][::-1]
