def group_check(s):
    l = 9223372036854775807
    while l > len(s):
        l = len(s)
        s = s.replace('()', '')
        s = s.replace('{}', '')
        s = s.replace('[]', '')
    return len(s) == 0
