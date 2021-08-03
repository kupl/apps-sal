import re


def solve(s):
    return max([int(i) for i in re.split('[^0-9]', s) if i != ''])
