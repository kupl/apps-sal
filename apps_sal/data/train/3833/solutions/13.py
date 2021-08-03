def longest(s1, s2):
    return "".join([x for x in "abcdefghijklmnopqrstuvwxyz" if x in s1 + s2])
