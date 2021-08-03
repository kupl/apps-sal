def is_in_middle(s):
    while len(s) > 4:
        s = s[1:-1]
    return 'abc' in s
