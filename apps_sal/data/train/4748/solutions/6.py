def insert_dash2(num):
    import re
    return re.sub('([2468])(?=[2468])', '\\1*', re.sub('([13579])(?=[13579])', '\\1-', str(num)))
