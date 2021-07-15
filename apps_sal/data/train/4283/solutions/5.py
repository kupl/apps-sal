def add(s1, s2):
    char_sum = lambda x: sum(map(ord, x))
    return char_sum(s1) + char_sum(s2)
