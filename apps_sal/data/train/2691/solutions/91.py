def solve(s):
    import re
    return max([int(i) for i in re.split('(\d+)', s) if i.isnumeric()])
