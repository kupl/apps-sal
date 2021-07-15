def is_in_middle(s):
    return is_in_middle(s[1:-1]) if s[4:] else 'abc' in s
