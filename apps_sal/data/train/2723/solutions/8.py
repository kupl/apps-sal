def average_string(s):
    (d, c) = ('zero one two three four five six seven eight nine'.split(), 0)
    for i in s.split():
        if i not in d:
            return 'n/a'
        c += d.index(i)
    return d[int(c / len(s.split()))] if s else 'n/a'
