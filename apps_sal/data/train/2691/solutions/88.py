def solve(s):
    import re
    return max(int(el) for el in re.findall(r'\d+', s))
