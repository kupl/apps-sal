def min_value(digits):
    s = ''
    for i in sorted(digits):
        if str(i) not in s:
            s += str(i)
    return int(s)
