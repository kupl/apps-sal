def solve(s):
    import re
    lst = [i for i in re.split('(\\d+)', s) if i.isnumeric()]
    max_num = 0
    for l in lst:
        if int(l) > max_num:
            max_num = int(l)
    return max_num
