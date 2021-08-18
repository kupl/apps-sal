def string_clean(s):
    junk = [str(i) for i in range(10)]
    new_s = ''
    for i in s:
        if i not in junk:
            new_s += i
    return new_s
