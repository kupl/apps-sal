import re

def split_odd_and_even(n):
    return [int(group[0] or group[1]) for group in re.findall(r'([13579]+)|([2468]+)', str(n))]
