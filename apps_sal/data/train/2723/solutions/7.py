s2d = 'zero one two three four five six seven eight nine'.split()


def average_string(stg):
    lst = stg.split()
    if not stg or set(lst) - set(s2d):
        return 'n/a'
    return s2d[int(sum((s2d.index(s) for s in lst)) / len(lst))]
