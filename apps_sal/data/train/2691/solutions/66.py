import re  # Jai Shree Ram!!!


def solve(s):
    l = [int(i) for i in re.findall(r'(\d+)', s)]
    return max(l)
